from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user, Extending django login/logout
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
