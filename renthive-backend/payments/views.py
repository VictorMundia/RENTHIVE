from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .mpesa.utils import lipa_na_mpesa_online
from rest_framework.decorators import api_view

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
    print(request.data)  # Log the callback data for now
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})
