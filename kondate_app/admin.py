from django.contrib import admin
# from .models import Family, Recipe, RecipeIngredient
from .models import Recipe, RecipeIngredient, RecipeProcess, Menu
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    List_display = ['']

#
# @admin.register(Family)
# class FamilyAdmin(admin.ModelAdmin):
#     List_display = ['']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    List_display = ("name", "date")


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    List_display = ['']


@admin.register(RecipeProcess)
class RecipeProcessAdmin(admin.ModelAdmin):
    List_display = ['']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    List_display = ['']


# FamilyAdmin.list_display = ['name']
RecipeAdmin.list_display = ['name', 'image', 'comment']
RecipeIngredientAdmin.list_display = ['name']
RecipeProcessAdmin.list_display = ['process']
MenuAdmin.list_display = ['name', 'date', 'category']

