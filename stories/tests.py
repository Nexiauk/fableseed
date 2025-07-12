from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class SimpleViewTest(TestCase):
    def test_hello_world_stories_app(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello world")