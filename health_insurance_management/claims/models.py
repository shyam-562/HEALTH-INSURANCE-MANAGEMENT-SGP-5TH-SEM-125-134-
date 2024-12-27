
from django.db import models
from django.conf import settings
from policies.models import Policy
# Create your models here.

class Claim(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    details = models.TextField()
