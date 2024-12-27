from django.shortcuts import render
from .models import FAQ

# Create your views here.

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq_view.html', {'faqs': faqs})
