from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from settings.models import Profile


class ProfileViewSetSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', default='',
                                     read_only=True)
    last_name = serializers.CharField(source='user.last_name', default='',
                                      read_only=True)
    first_name = serializers.CharField(source='user.first_name', default='',
                                       read_only=True)
    email = serializers.CharField(source='user.email', default='',
                                  read_only=True)

    class Meta:
        model = Profile
        fields = ('bio', 'birthday', 'username', 'last_name', 'first_name', 'email')
