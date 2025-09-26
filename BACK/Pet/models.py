# Pet/models.py
from django.db import models
from django.utils import timezone
from User.models import User
from cloudinary.models import CloudinaryField  # Importamos CloudinaryField

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Perro'),
        ('cat', 'Gato'),
        ('bird', 'Ave'),
        ('other', 'Otro'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pets',
        limit_choices_to={'role__name': 'Client'}
    )

    image = CloudinaryField("image", null=True, blank=True)  # Imagen de la mascota

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.species}) - Dueño: {self.owner.email}"

    class Meta:
        db_table = "pet"
