from django.db import models
from accounts.models import CustomUser


class Family(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name="family_user")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Family, on_delete=models.CASCADE)
    # ingredient = models.CharField(max_length=30)
    process = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ingredient(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=30)
