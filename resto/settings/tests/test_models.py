from django.contrib.auth.models import User
from django.test import TestCase

from settings.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.profile = Profile.objects.create(user=self.user, bio='about user', birthday='1111-11-11')

    def test_last_name_label(self):
        field_label = self.profile._meta.get_field('bio').verbose_name
        profile_user = Profile.objects.get(id=1)
        self.assertEqual(field_label, 'bio')
        self.assertEqual(profile_user.user.username, self.user.username)
