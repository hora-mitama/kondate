from django.db import models
from django.contrib.auth.models import AbstractUser
# from kondate_app.models import Family


class CustomUser(AbstractUser):
    # family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True, blank=True, related_name="family_user")

    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'

    def __str__(self):
        return self.username

