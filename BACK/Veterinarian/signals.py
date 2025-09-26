# veterinarian/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import User
from .models import Veterinarian

@receiver(post_save, sender=User)
def create_veterinarian_profile(sender, instance, created, **kwargs):
    if created and instance.role and instance.role.name == "Vet":
        Veterinarian.objects.create(user=instance)
