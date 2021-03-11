from django.contrib import admin
# from .models import Family, Recipe, RecipeIngredient
from .models import Recipe, RecipeIngredient
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


# FamilyAdmin.list_display = ['name']
RecipeAdmin.list_display = ['name', 'date', 'family', 'image']
RecipeIngredientAdmin.list_display = ['name']
