from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutUsPageView


class HomePageTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home page')

    def test_home_url_resolves_view(self):
        url = resolve('/')
        self.assertEqual(url.func.view_class, HomePageView)

    def test_aboutus_pages(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_template(self):
        response = self.client.get(reverse('aboutus'))
        self.assertTemplateUsed(response, 'pages/aboutus.html')

    def test_aboutus_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us', status_code=200)

    def test_abouts_url_resolve_view(self):
        url = resolve('/aboutus/')
        self.assertEqual(url.func.view_class, AboutUsPageView)