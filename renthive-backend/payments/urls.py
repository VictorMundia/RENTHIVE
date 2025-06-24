from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, MpesaStkPushView, mpesa_callback, MpesaTransactionVerifyView

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('mpesa/callback/', mpesa_callback, name='mpesa_callback'),
    path('mpesa/stkpush/', MpesaStkPushView.as_view(), name='mpesa_stkpush'),
    path('payments/verify/', MpesaTransactionVerifyView.as_view(), name='mpesa_verify'),
    path('', include(router.urls)),
]
