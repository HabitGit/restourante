from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def authorize(request):
    if request.user.is_authenticated:
        return render(request, 'html/settings.html')
    else:
        return render(request, 'registration/login.html')