from django.test import TestCase
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from ..models import Memo, Project

class MemoViewsIndexTest(TestCase):
    """indexへのテストクラス"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.index_url = reverse_lazy('memo:index')

    def test_get_success(self):
        """アクセスに成功することを検証"""
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memo/index.html')
    
    def test_post_memo_success(self):
        """メモを作成できること(POSTできること)を検証"""
        params = {
            'content': 'Test',
            'project': 'Test Project',
        }
        response = self.client.post(self.index_url, params)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)

    def test_post_memo_failure(self):
        """メモを作成できないこと(POSTできないこと)を検証"""
        # パラメータにprojectを含めないので失敗する
        params = {
            'content': 'Test',
        }

        with self.assertRaises(IntegrityError):
            response = self.client.post(self.index_url, params)

class MemoViewsProjectTest(TestCase):
    """projectへのテストクラス"""

    def setUp(self):
        self.memo = Memo.objects.create(
            content='Test',
            project=Project.objects.create(name='Test Project'),
        )

    def test_get_success(self):
        """アクセスに成功することを検証"""
        project_url = reverse_lazy('memo:project', args=[self.memo.project.id])
        response = self.client.get(project_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memo/project.html')
    
    def test_post_memo_success(self):
        """メモを作成できること(POSTできること)を検証"""
        project_url = reverse_lazy('memo:project', args=[self.memo.project.id])
        params = {
            'content': 'Test2',
        }
        response = self.client.post(project_url, params)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, project_url)

    def test_post_memo_success(self):
        """メモを作成できないこと(POSTできないこと)を検証"""
        # パラメータにcontentを含めないので失敗する
        project_url = reverse_lazy('memo:project', args=[self.memo.project.id])
        params = {}

        with self.assertRaises(IntegrityError):
            response = self.client.post(project_url, params)
    
class MemoViewsUpdateMemoTest(TestCase):
    """update-memoへのテストクラス"""

    def setUp(self):
        self.memo = Memo.objects.create(
            content='Test',
            project=Project.objects.create(name='Test Project'),
        )

    def test_get_success(self):
        """アクセスに成功することを検証"""
        update_memo_url = reverse_lazy('memo:update-memo', args=[self.memo.id])
        response = self.client.get(update_memo_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memo/update_memo.html')
    
    def test_post_memo_success(self):
        """メモを更新できること(POSTできること)を検証"""
        update_memo_url = reverse_lazy('memo:update-memo', args=[self.memo.id])
        params = {
            'content': 'Test Updated',
            'project': 'Test Project',
        }
        response = self.client.post(update_memo_url, params)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, update_memo_url)
    
    def test_post_memo_failure(self):
        """メモを更新できないこと(POSTできないこと)を検証"""
        update_memo_url = reverse_lazy('memo:update-memo', args=[self.memo.id])
        params = {}

        with self.assertRaises(IntegrityError):
            response = self.client.post(update_memo_url, params)

class MemoViewsDeleteMemoTest(TestCase):
    """delete-memoへのテストクラス"""

    def setUp(self):
        self.memo = Memo.objects.create(
            content='Test',
            project=Project.objects.create(name='Test Project'),
        )

    def test_get_success(self):
        """アクセスに成功することを検証"""
        delete_memo_url = reverse_lazy('memo:delete-memo', args=[self.memo.id])
        response = self.client.get(delete_memo_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memo/delete_memo.html')
    
    def test_post_memo_success(self):
        """メモを削除できること(POSTできること)を検証"""
        delete_memo_url = reverse_lazy('memo:delete-memo', args=[self.memo.id])
        params = {
            'content': 'Test',
            'project': 'Test Project',
        }
        response = self.client.post(delete_memo_url, params)

        index_url = reverse_lazy('memo:index')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, index_url)