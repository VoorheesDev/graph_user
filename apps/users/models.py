from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager


class User(AbstractUser):
    """
    A model to represent a user. This model implements the authentication model.

    Email and password are required. Other fields are optional.
    """

    username = None
    email = models.EmailField(_("Email address"), unique=True)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["email"]

    def __str__(self):
        """Returns readable representation of the model."""

        return f"User {self.id}: {self.email}"
