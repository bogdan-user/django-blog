from django.test import TestCase
from django.urls import reverse

class BlogTests(TestCase):

    def setUp(self):
        url = reverse('blog_app:post_list')
        self.response = self.client.get(url)

    def test_post_list_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_list_homepage(self):
        self.assertTemplateUsed(self.response, "blog_app/list.html")

    def test_post_list_contains(self):
        self.assertContains(self.response, "Blog")

    def test_post_list_not_contains(self):
        self.assertNotContains(self.response, "I shouldn't be here.")
