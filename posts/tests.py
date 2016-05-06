from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from posts.views import post_list

class IndexPageViewTest(TestCase):
    def test_home_page_user_posts_with_user(self):
        request = HttpRequest()
        context = {'user_name': 'romulo'}
        response = post_list(request, context)
        observed_content = response.content.decode('utf8')
        expected_content = render_to_string('index.html', {'user_name':'romulo'})
        self.assertEqual(observed_content, expected_content)

    def test_home_page_user_posts_without_user(self):
        request = HttpRequest()
        context = {}
        response = post_list(request, context)
        observed_content = response.content.decode('utf8')
        expected_content = render_to_string('index.html', {})
        self.assertEqual(observed_content, expected_content)
