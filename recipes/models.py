from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.models import Profile


class Recipe(models.Model):

    CUISINE_CHOICES = [
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other'),
    ]

    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(10)],
        error_messages={
            'unique': "We already have a recipe with the same title!"
        },
        blank=False
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CUISINE_CHOICES,
        blank=False
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space.",
        blank=False
    )

    instructions = models.TextField(blank=False)

    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
        validators=[MinValueValidator(1)],
        blank=False
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
