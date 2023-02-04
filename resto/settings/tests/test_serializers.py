import json
from django.contrib.auth.models import User
from django.test import TestCase

from settings.models import Profile
from settings.serializers import ProfileViewSetSerializer


class ProfileViewSetSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user_name1', last_name='Petrov',
                                    first_name='Ivan', email='ivan@mail.com')
        user2 = User.objects.create(username='user_name2', last_name='Vakulenko',
                                    first_name='Vasili', email='vasili@mail.com')

        Profile.objects.create(user=user1, bio='about user1', birthday='1111-11-11')
        Profile.objects.create(user=user2, bio='about user2', birthday='1111-11-11')

        profiles = Profile.objects.all()
        data = ProfileViewSetSerializer(profiles, many=True).data
        expected_data = [
            {
                'bio': 'about user1',
                'birthday': '1111-11-11',
                'username': 'user_name1',
                'last_name': 'Petrov',
                'first_name': 'Ivan',
                'email': 'ivan@mail.com'
            },
            {
                'bio': 'about user2',
                'birthday': '1111-11-11',
                'username': 'user_name2',
                'last_name': 'Vakulenko',
                'first_name': 'Vasili',
                'email': 'vasili@mail.com'
            },
        ]
        json_data = json.dumps(data)
        json_expected_data = json.dumps(expected_data)
        self.assertEqual(json_data, json_expected_data)
