from django.test import TestCase
from ..models import Memo, Project

class MemoModelsTest(TestCase):

    def create_memo(self):
        self.memo = Memo.objects.create(
            content='Test',
            project=Project.objects.create(name='Test Project'),
        )

    def test_no_memos(self):
        """初期状態(メモ数:0)を確認"""
        self.assertEqual(Memo.objects.all().count(), 0)
        self.assertEqual(Project.objects.all().count(), 0)
    
    def test_reate_memo(self):
        """メモが登録されることをチェック"""
        self.create_memo()
        self.assertEqual(Memo.objects.all().count(), 1)
        self.assertEqual(Project.objects.all().count(), 1)
    
    def test_revrieve_memo(self):
        """メモを取得できることをチェック"""
        self.create_memo()
        memo = Memo.objects.get(content='Test')
        self.assertEqual(memo.content, 'Test')
        self.assertEqual(memo.project.__class__, Project)
    
    def test_retrieve_project(self):
        """プロジェクトを取得できることをチェック"""
        self.create_memo()
        project = Project.objects.get(name='Test Project')
        self.assertEqual(project.name, 'Test Project')
    
    def test_delete_memo(self):
        """メモを削除できることをチェック"""
        self.create_memo()
        self.memo.delete()
        self.assertEqual(Memo.objects.all().count(), 0)