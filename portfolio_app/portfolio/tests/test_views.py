from django.test import TestCase
from django.urls import reverse_lazy
from allauth.account.models import EmailAddress
from accounts.models import User

import os
from dotenv import load_dotenv

load_dotenv()

class PortfolioViewsIndexTest(TestCase):

    def setUp(self):
        self.index_url = reverse_lazy('portfolio:index')
    
    def create_user(self):
        """テスト用のユーザ作成"""
        self.user = User.objects.create(
            username='Dummy',
            email='dummy@example.com',
        )
        self.user.set_password(os.getenv('TESTUSER_PASSWORD'))
        self.user.save()
        # ログイン用ユーザのメール検証を済ませる
        EmailAddress.objects.create(
            email=self.user.email,
            verified=True, 
            primary=True,
            user_id=self.user.id
        )
    
    def login(self):
        """テスト用ユーザでログインを行う"""
        self.client.login(
            email=self.user.email,
            password=os.getenv('TESTUSER_PASSWORD')
        )

    def test_access_success(self):
        """ログイン後にindexページへのアクセスが成功することを検証"""
        self.create_user()
        self.login()
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')
    
    def test_access_failure(self):
        """未ログイン時にindexページへのアクセスが失敗することを検証"""
        response = self.client.get(self.index_url)
        self.assertNotEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'portfolio/index.html')