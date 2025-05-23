from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Cook"

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_vegan = models.BooleanField(default=False)
    calories = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name="dishes",
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="dishes",
    )
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return (
            f"{self.name} (price: {self.price}, dish_type: {self.dish_type})"
        )
