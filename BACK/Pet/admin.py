from django.contrib import admin
from django.utils.html import format_html
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "species", "breed", "age", "owner", "get_image", "created_at")
    search_fields = ("name", "species", "breed", "owner__email", "owner__first_name", "owner__last_name")
    list_filter = ("species", "created_at")
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at") 

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;" />',
                obj.image.url,
            )
        return "Sin imagen"
    get_image.short_description = "Imagen"
