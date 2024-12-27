# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Policy, PolicyStatus
from datetime import datetime

def available_policies(request):
    policies = Policy.objects.filter(available=True)
    return render(request, 'policies/available_policies.html', {'policies': policies})

def policy_details(request, policy_id):
    policy = get_object_or_404(Policy, id=policy_id)
    has_applied = request.user.is_authenticated and PolicyStatus.objects.filter(user=request.user, policy=policy).exists()
    
    if request.method == 'POST' and not has_applied:
        # Calculate the user's age from birthdate
        if request.user.birthdate:
            today = datetime.today()
            age = today.year - request.user.birthdate.year - ((today.month, today.day) < (request.user.birthdate.month, request.user.birthdate.day))
            
            if age >= policy.min_age:
                # Create a new policy status if the user applies
                PolicyStatus.objects.create(user=request.user, policy=policy, status='Pending')
                return redirect('policy_details', policy_id=policy.id)
            else:
                # Return an error message if the user does not meet the age requirement
                return render(request, 'policies/policy_details.html', {
                    'policy': policy,
                    'has_applied': has_applied,
                    'error': 'You do not meet the minimum age requirement for this policy.'
                })
        else:
            # Handle cases where the user does not have a birthdate
            return render(request, 'policies/policy_details.html', {
                'policy': policy,
                'has_applied': has_applied,
                'error': 'Your profile is missing the birthdate information.'
            })
    
    return render(request, 'policies/policy_details.html', {'policy': policy, 'has_applied': has_applied})

def policy_status(request):
    statuses = PolicyStatus.objects.filter(user=request.user)
    return render(request, 'policies/policy_status.html', {'statuses': statuses})
