
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('manage-policies/', views.manage_policies_view, name='manage_policies'),
    path('add-policy/', views.add_policy_view, name='add_policy'),
    path('edit-policy/<int:policy_id>/', views.edit_policy_view, name='edit_policy'),
    path('delete-policy/<int:policy_id>/', views.delete_policy_view, name='delete_policy'),
    path('manage-users/', views.manage_users_view, name='manage_users'),
    path('delete-user/<int:user_id>/', views.delete_user_view, name='delete_user'),
    path('applied-policies/', views.applied_policies_view, name='applied_policies'),
    path('approve-policy/<int:policy_id>/', views.approve_policy, name='approve_policy'),
    path('reject-policy/<int:policy_id>/', views.reject_policy, name='reject_policy'),
]
