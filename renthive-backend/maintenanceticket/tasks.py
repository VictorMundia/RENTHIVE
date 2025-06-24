from celery import shared_task

def send_notification(ticket_id, old_status, new_status):
    # Implement your notification logic here (email, push, etc.)
    print(f"Ticket {ticket_id} status changed from {old_status} to {new_status}")
