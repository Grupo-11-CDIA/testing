from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User, Role
from Pet.models import Pet   # 👈 importamos Pet


class PetInline(admin.TabularInline):  # Podés cambiar a StackedInline si preferís
    model = Pet
    extra = 1
    fields = ("name", "species", "breed", "age", "get_image")  # mostramos campos útiles
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="40" height="40" style="object-fit:cover;border-radius:5px;"/>',
                obj.image.url,
            )
        return "Sin imagen"
    get_image.short_description = "Imagen"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "phone",
        "get_image",
        "role",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "role")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("id",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Información personal", {"fields": ("first_name", "last_name", "address", "phone", "image", "role")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2", "role", "is_active", "is_staff"),
            },
        ),
    )

    filter_horizontal = ("groups", "user_permissions")
    inlines = [PetInline]   # 👈 agregamos la relación con Pet

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover;border-radius:5px;"/>',
                obj.image.url,
            )
        return "Sin imagen"
    get_image.short_description = "Imagen"

    # 🔹 Sobrescribo save_model para asociar el grupo según el rol
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.role and obj.role.group:
            obj.groups.clear()
            obj.groups.add(obj.role.group)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id_role", "name", "group")
    search_fields = ("name",)
