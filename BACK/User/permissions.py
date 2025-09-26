# permissions.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.apps import apps
from .models import Role

def create_groups_and_permissions():
    User = get_user_model()

    # 1️⃣ Crear grupos si no existen
    client_group, _ = Group.objects.get_or_create(name="Client")
    vet_group, _ = Group.objects.get_or_create(name="Vet")
    admin_group, _ = Group.objects.get_or_create(name="Admin")

    # 2️⃣ Asociar grupos a roles
    for role_name, group in [("Client", client_group), ("Vet", vet_group), ("Admin", admin_group)]:
        try:
            role = Role.objects.get(name=role_name)
            role.group = group
            role.save()
        except Role.DoesNotExist:
            print(f"Role '{role_name}' no existe, se omitió la asociación con grupo.")

    # 3️⃣ Obtener modelos y permisos
    Order = apps.get_model("orders", "Order")
    Product = apps.get_model("inventory", "Product")
    Category = apps.get_model("inventory", "Category")

    order_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Order))
    product_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Product))
    category_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Category))
    user_perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(User))

    # 4️⃣ Asignar permisos a grupos
    vet_group.permissions.set(order_perms | product_perms | category_perms | user_perms)
    all_permissions = Permission.objects.all()
    admin_group.permissions.set(all_permissions)

    # 5️⃣ Asignar permisos directos a usuarios según rol
    for user in User.objects.all():
        if not user.role:
            continue

        if user.role.name == "Vet":
            # Excluir permisos críticos de usuario
            user_perms_without_admin_vet = user_perms.exclude(
                codename__in=["add_user", "change_user", "delete_user"]
            )
            user.user_permissions.set(order_perms | product_perms | category_perms | user_perms_without_admin_vet)
            user.groups.add(vet_group)

        elif user.role.name == "Admin":
            user.user_permissions.set(all_permissions)
            user.groups.add(admin_group)

        elif user.role.name == "Client":
            user.groups.add(client_group)

    # 6️⃣ Asociar superusuario al grupo Admin
    superuser = User.objects.filter(is_superuser=True).first()
    if superuser:
        superuser.groups.add(admin_group)

    print("✅ Grupos, roles y permisos configurados correctamente.")
