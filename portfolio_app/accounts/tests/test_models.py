from django.test import TestCase
from ..models import User

class AccountsModelsTest(TestCase):

    def test_should_be_no_users(self):
        """初期状態(ユーザ数:0)を確認"""
        self.assertEqual(User.objects.all().count(), 0)
    
    def test_should_create_user(self):
        """1ユーザの登録をチェック"""
        user = User(username='Test', email='test@example.com')
        user.save()
        self.assertEqual(User.objects.all().count(), 1)
    
    def test_create_and_retrieve_user(self):
        """ユーザ作成後にユーザを取得できることをチェック"""
        username = 'Test'
        email = 'test@example.com'
        user = User(username=username, email=email)
        user.save()

        saved_user = User.objects.get(username=username)

        self.assertEqual(saved_user.username, username)
        self.assertEqual(saved_user.email, email)
    
    def test_create_and_remove_user(self):
        """ユーザ作成後にユーザを削除できることをチェック"""
        user = User(username='Test', email='test@example.com')
        user.save()
        self.assertEqual(User.objects.all().count(), 1)

        saved_user = User.objects.get(username='Test')
        saved_user.delete()
        self.assertEqual(User.objects.all().count(), 0)
