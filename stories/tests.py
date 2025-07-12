from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SimpleViewTest(TestCase):
    """
    A class of tests designed specifically to test each view as its created.
    Tests that the view returns an HTTP 200 status code and contains the 
    text 'Hello world" in the response
    """
    def test_hello_world_index_view(self):
        """
        Tests that the index view in the stories app returns an HTTP 200 response code.
        Tests that it contains "Hellow world" in the response.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello world")