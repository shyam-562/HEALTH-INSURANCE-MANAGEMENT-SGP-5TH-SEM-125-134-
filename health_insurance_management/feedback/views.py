from django.shortcuts import render,redirect
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})
