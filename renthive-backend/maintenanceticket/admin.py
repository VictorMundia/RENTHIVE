from django.contrib import admin
from .models import MaintenanceTicket, Attachment

admin.site.register(MaintenanceTicket)
admin.site.register(Attachment)
