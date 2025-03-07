from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    type = models.IntegerField(verbose_name="صلاحية الحساب", default=0)

    def __str__(self):
        return self.username
