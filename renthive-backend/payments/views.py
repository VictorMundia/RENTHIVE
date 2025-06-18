from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .mpesa.utils import lipa_na_mpesa_online, get_access_token
from rest_framework.decorators import api_view
from .tasks import handle_mpesa_callback_async
from django.conf import settings
from datetime import datetime
import base64
import requests

# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class MpesaStkPushView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        amount = request.data.get('amount')
        account_reference = request.data.get('account_reference', 'RentHive')
        transaction_desc = request.data.get('transaction_desc', 'Payment')
        callback_url = 'https://happy-dancers-clap.loca.lt/api/mpesa/callback/'
        result = lipa_na_mpesa_online(phone, amount, account_reference, transaction_desc, callback_url)
        return Response(result)

@api_view(['POST'])
def mpesa_callback(request):
    # Safaricom will POST payment result here
    data = request.data
    handle_mpesa_callback_async.delay(data)
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})

class MpesaTransactionVerifyView(APIView):
    def post(self, request):
        checkout_request_id = request.data.get('CheckoutRequestID')
        if not checkout_request_id:
            return Response({'error': 'CheckoutRequestID is required'}, status=400)
        access_token = self.get_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
        if getattr(settings, 'MPESA_ENV', 'sandbox') == 'production':
            api_url = "https://api.safaricom.co.ke/mpesa/stkpushquery/v1/query"
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(
            (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()
        ).decode()
        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "CheckoutRequestID": checkout_request_id
        }
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.post(api_url, json=payload, headers=headers)
        return Response(response.json())

    def get_access_token(self):
        return get_access_token()
