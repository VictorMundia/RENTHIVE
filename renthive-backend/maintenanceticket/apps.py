from django.apps import AppConfig


class MaintenanceticketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maintenanceticket'

    def ready(self):
        import maintenanceticket.models  # noqa
