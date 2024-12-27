from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
