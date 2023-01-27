from django.urls import path

from . import views

urlpatterns = [
    path('', views.is_authenticated, name='is_authenticated'),
    path('registration', views.registration, name='registration'),
]