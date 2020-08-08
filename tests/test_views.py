from django.test import TestCase
from django.urls import reverse


class DeepThoughtTestCase(TestCase):

    def test_view(self):
        response = self.client.get(reverse("test_view"))
        self.assertEqual(response.content, b"test view")