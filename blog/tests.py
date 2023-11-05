from django.test import TestCase
from django.urls import reverse,resolve
from .views import PostListView
class TestUrl(TestCase):

    def test_blog_index_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEquals(resolve(url).func.view_class,PostListView)
