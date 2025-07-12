from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SimpleViewTest(TestCase):
    """
    A class of tests designed specifically to test each view as it's created.
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

class NurseryViewTests(TestCase):
    """
    A class of tests ensuring that the Nursery page loads successfully and displays all expected content.

    """
    def test_nursery_html_template(self):
        """Test that the nursery page loads successfully,
        uses the correct template, and contains expected text.
        Returns an HTTP 200 response.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "stories/nursery.html")
        self.assertContains(response, "Hello World, this is my new html page for the nursery")