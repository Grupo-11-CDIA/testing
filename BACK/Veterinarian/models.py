from django.db import models
from User.models import User
from cloudinary.models import CloudinaryField  # Importamos CloudinaryField

class Veterinarian(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="veterinarian")
    specialization = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = CloudinaryField("image", null=True, blank=True)  # Imagen del veterinario
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "veterinarian"
        verbose_name = "Veterinarian"
        verbose_name_plural = "Veterinarians"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.specialization or 'General'}"
