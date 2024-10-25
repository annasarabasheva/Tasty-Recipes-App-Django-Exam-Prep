from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import name_validator


class Profile(models.Model):
    nickname = models.CharField(
        unique=True,
        max_length=20,
        validators=[MinLengthValidator(2, message="Nickname must be at least 2 chars long!")],
        blank=False
    )

    first_name = models.CharField(
        max_length=30,
        validators=[name_validator],
        blank=False
    )

    last_name = models.CharField(
        max_length=30,
        validators=[name_validator],
        blank=False
    )

    chef = models.BooleanField(
        default=False,
        blank=False
    )

    bio = models.TextField(
        null=True,
        blank=True
    )
