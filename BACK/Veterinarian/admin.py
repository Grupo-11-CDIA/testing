from django.contrib import admin
from django.utils.html import format_html
from .models import Veterinarian

@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "specialization", "license_number", "phone", "get_image", "created_at")
    search_fields = ("user__email", "user__first_name", "user__last_name", "specialization", "license_number")
    list_filter = ("specialization", "created_at")
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url,
            )
        return "Sin imagen"
    get_image.short_description = "Imagen"
