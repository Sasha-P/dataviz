from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory

from ..views import HomeView


class HomePageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_root_url_resolves_to_home_page_view(self):
        request = self.factory.get(reverse('dataviz:home'))
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_home_page_returns_correct_html(self):
        request = self.factory.get(reverse('dataviz:home'))
        response = HomeView.as_view()(request)
        response.render()
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>DataViz | Home</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
