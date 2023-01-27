from django.shortcuts import render


def settings(request):
    return render(request, 'html/settings.html')

def profile(request):
    return render(request, 'html/profile.html')
