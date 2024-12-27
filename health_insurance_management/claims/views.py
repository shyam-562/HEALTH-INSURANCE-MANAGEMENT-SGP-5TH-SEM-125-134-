
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Claim

# Create your views here.

@login_required
def claims(request):
    user_claims = Claim.objects.filter(user=request.user)
    return render(request, 'claims/claims.html', {'claims': user_claims})
