from django.db import models
from django.conf import settings
# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    min_age = models.IntegerField(default=18)

class PolicyStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.policy.name} - {self.status}"