from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        required_fields = ['username', 'email', 'password', 'role', 'phone']
        for field in required_fields:
            if not data.get(field):
                return Response({'error': f'{field} is required.'}, status=status.HTTP_400_BAD_REQUEST)
        if data['password'] != data.get('confirm_password'):
            return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=data['email']).exists():
            return Response({'error': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=data['username']).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(phone=data['phone']).exists():
            return Response({'error': 'Phone number already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            role=data['role'],
            phone=data['phone'],
            national_id=data.get('national_id'),
            profile_picture=request.FILES.get('profile_picture'),
            password=make_password(data['password']),
        )
        return Response({'success': 'Registration successful!'}, status=status.HTTP_201_CREATED)
