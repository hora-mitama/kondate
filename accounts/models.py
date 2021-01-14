from django.db import models
from django.contrib.auth.models import AbstractUser

# from kondate_app.models import Family


class CustomUser(AbstractUser):
    family = models.ForeignKey("kondate_app.Family", on_delete=models.PROTECT, null=True, blank=True, related_name="family_user")

    class Meta:
        verbose_name_plural = 'CustomUser'

