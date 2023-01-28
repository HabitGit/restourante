from django.urls import path


from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    # path('profile/', views.profile, name='profile')
]