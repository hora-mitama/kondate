from django.db import models


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
    memo = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateField()

    CATEGORY_CHOICES = [
        ('main_dish', '主菜'),
        ('side_dish', '副菜'),
        ('soup', '汁物'),
        ('rice_dish', '飯物'),
        ('dessert', 'デザート'),
        ('drink', '飲み物'),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'

    def __str__(self):
        return self.name
