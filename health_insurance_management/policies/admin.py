from django.contrib import admin
from .models import Policy,PolicyStatus
# Register your models here.

admin.site.register(Policy)
admin.site.register(PolicyStatus)