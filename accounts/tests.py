from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountsTests(TestCase):

    def test_signup_page_url(self):
        urls = reverse('signup')
        response = self.client.get(urls)

        self.assertEqual(response.status_code, 200)

        used_templates = [t.name for t in response.templates if t.name]
        # print(used_templates)
        self.assertIn('registration/signup.html', used_templates)

        self.assertTemplateUsed(response, template_name='registration/signup.html')
        self.assertContains(response, '<h1>SIGNUP_PAGE</h1>')

    def test_signup_post_creates(self):
        deta = {
            'username': 'ali',
            'email': 'ali@ali.com',
            'password1': 'ali23222222',
            'password2': 'ali23222222',
        }
        response = self.client.post(reverse('signup'), deta)
        self.assertEqual(response.status_code, 302)
        # print(response.context['form'].errors)
        self.assertRedirects(response, reverse('login'))

        User = get_user_model()
        self.assertTrue(User.objects.filter(username=deta['username']).exists())

        user = User.objects.get(username=deta['username'])
        self.assertEqual(user.email, deta['email'])

    def test_login_page_url(self):
        urls = reverse('login')
        response = self.client.get(urls)
        self.assertEqual(response.status_code, 200)


