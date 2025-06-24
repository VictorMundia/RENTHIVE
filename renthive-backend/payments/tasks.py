from celery import shared_task
import requests

def process_mpesa_payment_callback(data):
    # Here you can process and store the callback data as needed
    # For now, just print or log it
    print('Processing MPESA callback:', data)

@shared_task
def handle_mpesa_callback_async(data):
    process_mpesa_payment_callback(data)
