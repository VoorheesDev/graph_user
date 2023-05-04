from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


USER_MODEL = get_user_model()


@admin.register(USER_MODEL)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "email",
        "is_staff",
        "is_active",
        "last_login",
        "date_joined",
    )
    list_display_links = ("id", "email")
    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    ordering = ("email",)
    list_per_page = 30
    fieldsets = (
        (_("Login info"), {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (_("Login info"), {"fields": ("email", "password1", "password2")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "groups", "user_permissions")}),
    )
