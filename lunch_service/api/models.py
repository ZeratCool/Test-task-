import uuid

from django.db import models

from accounts.models import CasualUser


class Restaurant(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name="name", max_length=100)
    address = models.CharField(verbose_name="address", max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return f'{self.name} ({self.address})'


class Menu(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    name = models.CharField(verbose_name="name", max_length=100)
    description = models.TextField(verbose_name="description", blank=True, null=True)
    image = models.ImageField(verbose_name="image", upload_to="media/files/%Y/%m/%d", blank=True, null=True)
    restaurants = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True , verbose_name="Restaurants")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
    def __str__(self):
        return f'{self.name} ({self.restaurants})'


class Vote(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=
                                    models.CASCADE, blank=True, null=True)

    user = models.ForeignKey(CasualUser, on_delete=
                                    models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f'{self.restaurant.name} - {self.user}'
