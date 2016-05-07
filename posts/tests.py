from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.test import Client
from posts.views import post_list, post_detail
from .models import Post


class PostDatailViewTest(TestCase):

    def setUp(self):
        post = Post(title="Meu primeiro post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a sollicitudin ex. Quisque sit amet magna lacus. Integer lobortis ligula orci, at tempus nisl blandit in. Fusce risus tellus, porttitor lobortis quam a, elementum egestas metus. Pellentesque quis lectus mattis elit hendrerit consequat. Donec quis tincidunt ante. Integer fermentum feugiat ipsum sit amet dignissim. Sed faucibus risus turpis, at rhoncus massa porttitor vitae. Etiam aliquet elit vitae dolor imperdiet pellentesque. Sed in gravida diam, et rhoncus orci. Maecenas laoreet arcu sed nibh ornare vestibulum. Nullam tempus semper diam, vel lobortis odio convallis in. Etiam aliquam aliquam malesuada. Phasellus a hendrerit risus. Suspendisse dignissim laoreet maximus.")
        post.save()
        post = Post(title="AE2", content="Ê2 Ê2 Ê2 Ê2")
        post.save()

    def test_post_detail_found(self):
        request = HttpRequest()
        response = post_detail(request, 1)
        observed_content = response.content.decode('utf8')
        instance = get_object_or_404(Post, id=1)
        context = {
            "title": "Detail",
            "instance": instance,
        }
        expected_content = render_to_string('post_detail.html', context)
        self.assertEqual(observed_content, expected_content)

    def test_post_list_filled(self):
        c = Client()
        response = c.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_title(self):
        c = Client()
        response = c.get('/posts/detail/1/')
        context = response.context
        instance = context['instance']
        self.assertEqual(instance.title, "Meu primeiro post")

    def test_post_detail_found(self):
        c = Client()
        response = c.get('/posts/detail/1/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_not_found(self):
        c = Client()
        response = c.get('/posts/detail/99/')
        self.assertEqual(response.status_code, 404)

    def test_post_list_emtpy(self):
        c = Client()
        Post.objects.all().delete()
        response = c.get('/posts/')
        self.assertEqual(response.status_code, 404)
