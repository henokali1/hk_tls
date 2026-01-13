from django.shortcuts import render
from .models import ExternalApp

def index(request):
    apps = ExternalApp.objects.filter(is_active=True)
    return render(request, 'dashboard/index.html', {'apps': apps})
