
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile

class UserProfileTests(APITestCase):
    def test_create_user_profile(self):
        url = reverse('profile-create')
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'bio': 'Hello, I am John Doe.',
            'profile_picture': None
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().name, 'John Doe')

    def test_update_user_profile(self):
        user_profile = UserProfile.objects.create(name='John Doe', email='john@example.com')
        url = reverse('profile-update', args=[user_profile.id])
        data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'bio': 'Hello, I am Jane Smith.',
            'profile_picture': None
        }

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserProfile.objects.get().name, 'Jane Smith')
