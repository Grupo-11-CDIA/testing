# Veterinarian/apps.py
from django.apps import AppConfig

class VeterinarianConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Veterinarian'

    def ready(self):
        import Veterinarian.signals
