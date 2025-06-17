import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    if getattr(settings, 'MPESA_ENV', 'sandbox') == 'production':
        url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(url, auth=HTTPBasicAuth(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    return r.json().get('access_token')

def lipa_na_mpesa_online(phone_number, amount, account_reference, transaction_desc, callback_url=None):
    access_token = get_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()
    ).decode()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    if getattr(settings, 'MPESA_ENV', 'sandbox') == 'production':
        api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {access_token}"}
    if not callback_url:
        callback_url = 'https://happy-dancers-clap.loca.lt/api/mpesa/callback/'
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
