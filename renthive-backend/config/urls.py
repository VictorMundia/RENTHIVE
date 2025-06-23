"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from views import (
    home, login_view, register_view, dashboard_view, #properties_view,
      property_detail_view,
    tenants_view, leases_view, payments_view, maintenance_view, messages_view, notifications_view, profile_view,
    proof_of_ownership_view, add_property_view, tenant_register_view
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    #path('properties/', properties_view, name='properties'),
    path('properties/<int:id>/', property_detail_view, name='property_detail'),
    path('tenants/', tenants_view, name='tenants'),
    path('leases/', leases_view, name='leases'),
    path('payments/', payments_view, name='payments'),
    path('maintenance/', maintenance_view, name='maintenance'),
    path('messages/', messages_view, name='messages'),
    path('notifications/', notifications_view, name='notifications'),
    path('profile/', profile_view, name='profile'),
    path('admin/', admin.site.urls),
    path('api/', include('properties.urls')),
    path('api/', include('leases.urls')),
    path('api/', include('messaging.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('unit.urls')),
    path('api/', include('receipt.urls')),
    path('api/', include('propertytype.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('user.urls')),
    path('api/', include('maintenanceticket.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('proof-of-ownership/', proof_of_ownership_view, name='proof_of_ownership'),
    path('add-property/', add_property_view, name='add_property'),
    path('api/', include('user.api_urls')),
    path('tenant-register/', tenant_register_view, name='tenant_register'),
]

urlpatterns += [
    path('property/<int:property_id>/', property_detail_view, name='property_detail'),
    path('tenants/', tenants_view, name='tenants'),
    path('leases/', leases_view, name='leases'),
    path('payments/', payments_view, name='payments'),
    path('maintenance/', maintenance_view, name='maintenance'),
    path('messages/', messages_view, name='messages'),
    path('notifications/', notifications_view, name='notifications'),
    path('profile/', profile_view, name='profile'),
]
