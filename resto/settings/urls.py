from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', views.settings, name='settings'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile2')
 ]

urlpatterns += router.urls
