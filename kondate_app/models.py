from django.db import models
from django.utils import timezone


class Family(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Family'

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="menu_family")
    date = models.DateField(default=timezone.now)

    CATEGORY_CHOICES = [
        ('main_dish', '主菜'),
        ('side_dish', '副菜'),
        ('soup', '汁物'),
        ('rice_dish', '飯物'),
        ('dessert', 'デザート'),
        ('drink', '飲み物'),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10, default="main_dish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class Memo(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    memo = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Memo'
        verbose_name_plural = 'Memo'

    def __str__(self):
        return self.memo


class Ingredient(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="amount")
    amount = models.IntegerField()

    class Meta:
        verbose_name = 'Amount'
        verbose_name_plural = 'Amount'

