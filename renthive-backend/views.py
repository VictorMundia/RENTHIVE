from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def properties_view(request):
    return render(request, 'properties.html')

def property_detail_view(request):
    return render(request, 'property_detail.html')

def tenants_view(request):
    return render(request, 'tenants.html')

def leases_view(request):
    return render(request, 'leases.html')

def payments_view(request):
    return render(request, 'payments.html')

def maintenance_view(request):
    return render(request, 'maintenance.html')

def messages_view(request):
    return render(request, 'messages.html')

def notifications_view(request):
    return render(request, 'notifications.html')

def profile_view(request):
    return render(request, 'profile.html')
