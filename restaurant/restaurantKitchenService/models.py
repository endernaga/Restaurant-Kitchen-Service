from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("restaurant:dishTypes_detail", kwargs={"pk": self.pk})


class Cook(AbstractUser):
    year_of_expirience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "cooker"
        verbose_name_plural = "cookers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cookers_detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dish_type")
    cooks = models.ManyToManyField(Cook, related_name="cooks")

    def get_absolute_url(self):
        return reverse("restaurant:dish_view", kwargs={"pk": self.pk})
