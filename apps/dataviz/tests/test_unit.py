from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser, User

from ..views import HomeView


class HomePageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='top_secret')

    def test_root_url_redirect_to_login_page(self):
        request = self.factory.get(reverse('dataviz:home'), follow=True)
        request.user = AnonymousUser()
        response = HomeView.as_view()(request)
        response.client = Client()
        self.assertRedirects(response, '/login/?next=/')

    def test_home_page_returns_correct_html(self):
        response = self.client.login(username='test', password='top_secret')
        self.assertTrue(response)

        response = self.client.get(reverse('dataviz:home'), follow=True)
        # request.user = AnonymousUser()
        # response = HomeView.as_view()(request)
        # response.render()
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'), response.content)
        self.assertIn(b'<title>DataViz | Home</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

        self.client.logout()

    def test_login_page_returns_correct_html(self):
        response = self.client.get(reverse('login'), follow=True)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>DataViz | Login</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
