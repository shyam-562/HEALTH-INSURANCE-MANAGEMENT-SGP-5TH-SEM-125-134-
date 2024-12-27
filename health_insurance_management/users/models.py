from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=255, blank=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return self.username