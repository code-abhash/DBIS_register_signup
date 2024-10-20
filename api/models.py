
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    mobile_no = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.username
