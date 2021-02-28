from django.contrib import admin
from .models import Family, Menu, MenuIngredient
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    List_display = ['']


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    List_display = ['']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    List_display = ("name", "date")


@admin.register(MenuIngredient)
class MenuIngredientAdmin(admin.ModelAdmin):
    List_display = ['']


FamilyAdmin.list_display = ['name']
MenuAdmin.list_display = ['name', 'date']
MenuIngredientAdmin.list_display = ['name']
