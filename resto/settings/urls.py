from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.settings, name='settings'),
 ]

urlpatterns += router.urls
