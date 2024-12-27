from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from policies.models import Policy, PolicyStatus
from claims.models import Claim

User = get_user_model()

# Function to check if the user is an admin
def is_admin(user):
    return user.is_staff  # or use user.is_superuser if you want stricter control

@login_required
def dashboard(request):
    user_claims = Claim.objects.filter(user=request.user)
    policies = Policy.objects.filter(approved=True, available=True)
    return render(request, 'dashboard/dashboard.html', {'claims': user_claims, 'policies': policies})

def home(request):
    return render(request, 'home.html')

# Admin dashboard view
@user_passes_test(is_admin, login_url='adminlogin')
def admin_dashboard_view(request):
    context = {
        'total_users': User.objects.all().count(),
        'total_policies': Policy.objects.all().count(),
        'approved_policies': PolicyStatus.objects.filter(status='Approved').count(),
        'pending_policies': PolicyStatus.objects.filter(status='Pending').count(),
        'rejected_policies': PolicyStatus.objects.filter(status='Rejected').count(),
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

# View to manage policies
@user_passes_test(is_admin, login_url='adminlogin')
def manage_policies_view(request):
    policies = Policy.objects.all()
    return render(request, 'dashboard/manage_policies.html', {'policies': policies})

# View to manage users
@user_passes_test(is_admin, login_url='adminlogin')
def manage_users_view(request):
    users = User.objects.all()
    return render(request, 'dashboard/manage_users.html', {'users': users})

# Approve policy
@user_passes_test(is_admin, login_url='adminlogin')
def approve_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    policy_status = PolicyStatus.objects.get(policy=policy)
    policy_status.status = 'Approved'
    policy_status.save()
    return redirect('applied_policies')

# Reject policy
@user_passes_test(is_admin, login_url='adminlogin')
def reject_policy(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    policy_status = PolicyStatus.objects.get(policy=policy)
    policy_status.status = 'Rejected'
    policy_status.save()
    return redirect('applied_policies')

# Add new policy
@user_passes_test(is_admin, login_url='adminlogin')
def add_policy_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        available = request.POST.get('available') == 'on'
        premium = request.POST.get('premium')
        min_age = request.POST.get('min_age')

        new_policy = Policy.objects.create(
            name=name, 
            description=description,
            available=available, 
            premium=premium,
            min_age=min_age
        )
        new_policy.save()
        return redirect('manage_policies')

    return render(request, 'dashboard/add_policy.html')

# Edit existing policy
@user_passes_test(is_admin, login_url='adminlogin')
def edit_policy_view(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    if request.method == 'POST':
        policy.name = request.POST.get('name')
        policy.description = request.POST.get('description')
        policy.available = request.POST.get('available') == 'on'
        policy.approved = request.POST.get('approved') == 'on'
        policy.min_age = request.POST.get('min_age')
        policy.save()
        return redirect('manage_policies')
    return render(request, 'dashboard/edit_policy.html', {'policy': policy})

# Delete policy
@user_passes_test(is_admin, login_url='adminlogin')
def delete_policy_view(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    policy.delete()
    return redirect('manage_policies')

# Delete user
@user_passes_test(is_admin, login_url='adminlogin')
def delete_user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')

@user_passes_test(is_admin, login_url='adminlogin')
def applied_policies_view(request):
    applied_policies = PolicyStatus.objects.filter(status='Pending')  # Fetch PolicyStatus instances
    return render(request, 'dashboard/applied_policies.html', {'applied_policies': applied_policies})