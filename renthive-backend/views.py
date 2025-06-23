from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from user.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.urls import reverse
from properties.models import Property
from properties.forms import PropertyForm

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def dashboard_view(request):
    properties = []
    form = None
    if request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'OWNER':
        properties = Property.objects.filter(owner=request.user)
        if request.method == 'POST':
            form = PropertyForm(request.POST)
            if form.is_valid():
                prop = form.save(commit=False)
                prop.owner = request.user
                prop.save()
                messages.success(request, 'Property added successfully!')
                return redirect('dashboard')
        else:
            form = PropertyForm()
    context = {
        'properties': properties,
        'form': form,
    }
    return render(request, 'dashboard.html', context)

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

@csrf_protect
def proof_of_ownership_view(request):
    return render(request, 'proof_of_ownership.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        phone = request.POST.get('phone')
        national_id = request.POST.get('national_id')
        profile_picture = request.FILES.get('profile_picture')
        # Validation
        if not all([username, email, password, confirm_password, role, phone]):
            messages.error(request, 'All required fields must be filled.')
            return render(request, 'register.html')
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
        if User.objects.filter(phone=phone).exists():
            messages.error(request, 'Phone number already exists.')
            return render(request, 'register.html')
        user = User.objects.create(
            username=username,
            email=email,
            role=role,
            phone=phone,
            national_id=national_id,
            profile_picture=profile_picture,
            password=make_password(password),
        )
        if role == 'OWNER':
            messages.success(request, 'Registration successful! Please provide proof of property ownership.')
            return redirect('proof_of_ownership')
        else:
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    return render(request, 'register.html')
