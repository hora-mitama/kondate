from django.contrib import admin
from .models import Family, Menu, Ingredient, Memo
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


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    List_display = ['']


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    List_display = ['']


FamilyAdmin.list_display = ['name']
MenuAdmin.list_display = ['name', 'date']
IngredientAdmin.list_display = ['name', 'amount']
MemoAdmin.list_display = ['memo']
