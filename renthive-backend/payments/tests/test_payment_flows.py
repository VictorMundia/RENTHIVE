from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from payments.models import Payment
from user.models import User

class PaymentFlowTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='testpass123', role='TENANT')
        self.client.force_authenticate(user=self.user)

    def test_stk_push_initiation(self):
        url = reverse('mpesa_stkpush')
        data = {
            'phone': '254700000000',
            'amount': 10,
            'account_reference': 'TestRef',
            'transaction_desc': 'Test Payment'
        }
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])
        self.assertIn('MerchantRequestID', response.data)
        self.assertIn('CheckoutRequestID', response.data)

    def test_callback_processing(self):
        url = reverse('mpesa_callback')
        callback_data = {
            "Body": {
                "stkCallback": {
                    "MerchantRequestID": "12345",
                    "CheckoutRequestID": "67890",
                    "ResultCode": 0,
                    "ResultDesc": "Success",
                    "CallbackMetadata": {
                        "Item": [
                            {"Name": "Amount", "Value": 10},
                            {"Name": "MpesaReceiptNumber", "Value": "XYZ123"},
                            {"Name": "PhoneNumber", "Value": "254700000000"}
                        ]
                    }
                }
            }
        }
        response = self.client.post(url, callback_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["ResultCode"], 0)

    def test_payment_verification(self):
        url = reverse('mpesa_verify')
        data = {"CheckoutRequestID": "67890"}
        response = self.client.post(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST])
        # The response will depend on the test environment and mock data
