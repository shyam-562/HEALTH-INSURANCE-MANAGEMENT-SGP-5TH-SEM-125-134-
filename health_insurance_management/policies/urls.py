
from django.urls import path
from . import views

urlpatterns = [
    path('', views.available_policies, name='available_policies'),
    path('<int:policy_id>/', views.policy_details, name='policy_details'),
    path('policy-status/', views.policy_status, name='policy_status'),
]
