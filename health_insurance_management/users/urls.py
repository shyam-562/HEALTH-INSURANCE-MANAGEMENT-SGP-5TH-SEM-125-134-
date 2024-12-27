
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('logout/', views.logout, name='logout'),
]
