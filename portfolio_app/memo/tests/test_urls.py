from django.test import TestCase
from django.urls import reverse_lazy, resolve
from .. import views

class MemoUrlsTest(TestCase):

    def test_index_url(self):
        """memo:index のURLテスト"""
        url = reverse_lazy('memo:index')
        self.assertEqual(resolve(url).func, views.index)
    
    def test_project_url(self):
        """memo:project のURLテスト"""
        url = reverse_lazy('memo:project', args=[1])
        self.assertEqual(resolve(url).func, views.project)
    
    def test_update_memo_url(self):
        """memo:update-memo のURLテスト"""
        url = reverse_lazy('memo:update-memo', args=[1])
        self.assertEqual(resolve(url).func, views.update_memo)

    def test_delete_memo_url(self):
        """memo:delete-memo のURLテスト"""
        url = reverse_lazy('memo:delete-memo', args=[1])
        self.assertEqual(resolve(url).func, views.delete_memo)