from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user = models.TextField(blank=True, null=True)
