from django.contrib import admin
from .models import Family, Menu, Ingredient
from accounts.models import CustomUser

admin.site.register(Family)
admin.site.register(Menu)
admin.site.register(Ingredient)
admin.site.register(CustomUser)
