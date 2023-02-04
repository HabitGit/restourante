from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from settings.models import Profile
from settings.serializers import ProfileViewSetSerializer


class ProfileApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username')
        self.user2 = User.objects.create(username='test_username2')
        self.user3 = User.objects.create(username='test_username3')
        self.profile = Profile.objects.create(user=self.user, bio='about user', birthday='1111-11-11')
        self.profile2 = Profile.objects.create(user=self.user2, bio='about user 2', birthday='1111-11-11')

    def test_get(self):
        url = reverse('profile-list')
        self.client.force_login(self.user)
        response = self.client.get(url)
        profile = Profile.objects.filter(user=self.user)
        serializer_data = ProfileViewSetSerializer(profile, many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_create(self):
        self.assertEqual(2, Profile.objects.all().count())
        url = reverse('profile-list')
        data = {
            'bio': 'about user 3',
            'birthday': '1234-11-11',
        }
        self.client.force_login(self.user3)
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, Profile.objects.all().count())
        self.assertEqual(self.user3, Profile.objects.last().user)

    def test_create_not_user(self):
        self.assertEqual(2, Profile.objects.all().count())
        url = reverse('profile-list')
        data = {
            'bio': 'about user 3',
            'birthday': '1234-11-11',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(2, Profile.objects.all().count())

    def test_update(self):
        url = reverse('profile-detail', args=(self.profile.id,))
        data = {
            'bio': 'new text about user',
            'birthday': '1234-11-12',
        }
        self.client.force_login(self.user)
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.profile.refresh_from_db()
        self.assertEqual('new text about user', self.profile.bio)

    def test_update_not_user(self):
        url = reverse('profile-detail', args=(self.profile.id,))
        data = {
            'bio': 'new text about user',
            'birthday': '1234-11-12',
        }
        self.client.force_login(self.user3)
        response = self.client.put(url, data=data)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual('about user', self.profile.bio)
