from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    (1, "Admin"),
    (2, "Basic"),
    (3, "Guard"),
    (4, "Guest"),
)


class User(AbstractUser):
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=2)  # noqa E501
    email = models.EmailField(unique=True)
    avatar = ResizedImageField(
        size=[300, 300],
        upload_to="users/avatars/%Y/%m/",
        blank=True,
        null=True,  # noqa E501
    )

    REQUIRED_FIELDS = ["email"]
