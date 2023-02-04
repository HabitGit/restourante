from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from settings.models import Profile
from settings.serializers import ProfileViewSetSerializer


def settings(request):
    return render(request, 'html/settings.html')


class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileViewSetSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
