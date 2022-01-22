from pydoc import resolve
from django.test import TestCase
from django.urls import reverse_lazy, resolve
from .. import views

class PortfolioUrlsTest(TestCase):

    def test_index_url(self):
        """portfolio:index のURLテスト"""
        url = reverse_lazy('portfolio:index')
        self.assertEqual(resolve(url).func, views.index)