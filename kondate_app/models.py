from django.db import models
from django.utils import timezone
from accounts.models import CustomUser


class Recipe(models.Model):
    name = models.CharField(verbose_name='名前', max_length=100)
    user = models.ForeignKey(CustomUser, vorbose_name='ユーザー',
                             on_delete=models.CASCADE,
                             related_name='recipe_user')
    image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='写真',
                              height_field='url_height',
                              width_field='url_width',)
    url_height = models.IntegerField(editable=False,)
    url_width = models.IntegerField(editable=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'レシピ'
        verbose_name_plural = 'レシピ'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    name = models.CharField(verbose_name='材料', max_length=100)
    recipe = models.ForeignKey(Recipe, verbose_name='レシピ',
                               on_delete=models.CASCADE,
                               related_name="ingredient_Recipe")
    amount = models.CharField(verbose_name='数量', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '材料'
        verbose_name_plural = '材料'

    def __str__(self):
        return self.name


class RecipeProcess(models.Model):
    process = models.TextField(Recipe, max_length=200)
    recipe = models.ForeignKey(Recipe, verbose_name='レシピ',
                               on_delete=models.CASCADE,
                               related_name='process_Recipe')
    image = models.ImageField(upload_to='images/processes/%Y/%m/%d', verbose_name='写真',
                              height_field='url_height',
                              width_field='url_width',)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '作り方'
        verbose_name_plural = '作り方'

    def __str__(self):
        return self.process


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='献立')
    recipe = models.ForeignKey(Recipe, verbose_name='レシピ', on_delete=models.CASCADE,
                               related_name='menu_recipe')
    date = models.DateField(verbose_name='日付', default=timezone.now)

    CATEGORY_CHOICES = [
        ('main_dish', '主菜'),
        ('side_dish', '副菜'),
        ('soup', '汁物'),
        ('rice', '飯物'),
        ('dessert', 'デザート'),
        ('drink', '飲み物'),
    ]

    category = models.CharField(verbose_name='カテゴリー',
                                choices=CATEGORY_CHOICES,
                                max_length=10,
                                default="main_dish")

    class Meta:
        verbose_name = '献立'
        verbose_name_plural = '献立'

    def __str__(self):
        return self.name


# class Recipe(models.Model):
#     name = models.CharField(verbose_name='名前', max_length=100)
#     # family = models.ForeignKey(Family, verbose_name='家族', on_delete=models.CASCADE,
#     #                            related_name="recipe_family")
#     user = models.ForeignKey(CustomUser, vorbose_name='ユーザー', on_delete=models.CASCADE,
#                              related_name='recipe_user')
#     # date = models.DateField(verbose_name='日付', default=timezone.now)
#     image = models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='写真',
#                               height_field='url_height',
#                               width_field='url_width',)
#     url_height = models.IntegerField(editable=False,)
#     url_width = models.IntegerField(editable=False,)
#
#     # CATEGORY_CHOICES = [
#     #     ('main_dish', '主菜'),
#     #     ('side_dish', '副菜'),
#     #     ('soup', '汁物'),
#     #     ('rice', '飯物'),
#     #     ('dessert', 'デザート'),
#     #     ('drink', '飲み物'),
#     # ]
#     #
#     # category = models.CharField(verbose_name='カテゴリー',
#     #                             choices=CATEGORY_CHOICES,
#     #                             max_length=10,
#     #                             default="main_dish")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Recipe'
#         verbose_name_plural = 'Recipe'
#
#     def __str__(self):
#         return self.name


# class Family(models.Model):
#     name = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = 'Family'
#         verbose_name_plural = 'Family'
#
#     def __str__(self):
#         return self.name
