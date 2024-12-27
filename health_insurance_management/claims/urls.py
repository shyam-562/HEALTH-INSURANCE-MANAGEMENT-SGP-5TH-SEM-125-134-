from django.urls import path
from . import views

urlpatterns = [
    path('', views.claims, name='claims'),
]
