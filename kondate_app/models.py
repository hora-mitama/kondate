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
    name = models.CharField(verbose_name='名前', max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name="menu_family")
    date = models.DateField(verbose_name='日付', default=timezone.now)

    CATEGORY_CHOICES = [
        ('main_dish', '主菜'),
        ('side_dish', '副菜'),
        ('soup', '汁物'),
        ('rice', '飯物'),
        ('dessert', 'デザート'),
        ('drink', '飲み物'),
    ]

    category = models.CharField(verbose_name='カテゴリー', choices=CATEGORY_CHOICES, max_length=10, default="main_dish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.name


class MenuIngredient(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="ingredient_menu")
    name = models.CharField(verbose_name='材料', max_length=100)
    amount = models.CharField(verbose_name='数量', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'

    def __str__(self):
        return self.name


class MenuProcess(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='process_menu')
    process = models.TextField(Menu, max_length=200)
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '作り方'
        verbose_name_plural = '作り方'

    def __str__(self):
        return self.process
