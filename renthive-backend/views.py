from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from user.models import User
from properties.models import Property, ProofOfOwnership
import os


def register_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create(
                username=username,
                email=email,
                phone=phone,
                role=role,
                password=make_password(password),
                is_active=True
            )
            if role == "OWNER":
                login(request, user)
                return redirect('proof_of_ownership')
            else:
                messages.success(request, "Account created! Please log in.")
                return redirect('login')
    return render(request, 'register.html')

def tenant_register_view(request):
    if request.method == 'POST':
        role = 'TENANT'
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create(
                username=username,
                email=email,
                phone=phone,
                role=role,
                password=make_password(password),
                is_active=True
            )
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    return render(request, 'tenant_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

from google.cloud import vision

@login_required
def proof_of_ownership_view(request):
    if request.method == 'POST':
        document = request.FILES.get('ownership_proof')
        description = request.POST.get('description', '')

        if not document:
            messages.error(request, "No file uploaded.")
            return redirect('proof_of_ownership')

        ProofOfOwnership.objects.create(
            user=request.user,
            document=document,
            description=description,
            status='Pending Verification'
        )
        messages.success(request, "Proof of ownership submitted and is pending manual verification.")
        return redirect('profile')  # Redirect to profile after upload

    return render(request, 'proof_of_ownership.html')


@login_required
def dashboard_view(request):
    properties = None
    proof = None
    if request.user.role == 'OWNER':
        proof = ProofOfOwnership.objects.filter(user=request.user).order_by('-id').first()
        if not proof or proof.status != 'Verified':
            return redirect('proof_of_ownership')
        properties = Property.objects.filter(owner=request.user)
    elif request.user.role == 'TENANT':
        # Customize tenant dashboard logic here
        pass
    return render(request, 'dashboard.html', {
        'properties': properties,
        'proof': proof,
    })

@login_required
def add_property_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        unit_count = request.POST.get('unit_count')
        rent_amount = request.POST.get('rent_amount')
        Property.objects.create(
            owner=request.user,
            name=name,
            location=location,
            unit_count=unit_count,
            rent_amount=rent_amount
        )
        messages.success(request, "Property added!")
        return redirect('dashboard')
    return render(request, 'add_property.html')

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

@login_required
def property_detail_view(request, property_id):
    # Fetch property details by ID
    # property = Property.objects.get(id=property_id)
    return render(request, 'property_detail.html')  # Add context as needed

@login_required
def tenants_view(request):
    return render(request, 'tenants.html')

@login_required
def leases_view(request):
    return render(request, 'leases.html')

@login_required
def payments_view(request):
    return render(request, 'payments.html')

@login_required
def maintenance_view(request):
    return render(request, 'maintenance.html')

@login_required
def messages_view(request):
    return render(request, 'messages.html')

@login_required
def notifications_view(request):
    return render(request, 'notifications.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/renthive-7d89d-dd7446695ef6.json"
