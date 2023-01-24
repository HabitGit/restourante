from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required
def authorize(request):
    if request.user.is_authenticated:
        return render(request, 'html/login_page.html')
    else:
        return render(request, 'registration/login.html')