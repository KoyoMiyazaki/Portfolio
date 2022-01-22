from django.test import TestCase
from django.urls import reverse_lazy, resolve
from allauth.account.models import EmailAddress
from ..models import User

import os
from dotenv import load_dotenv

load_dotenv()

class AccountsViewsTest(TestCase):
    """各種viewへのテストの基底クラス"""

    def setUp(self):
        pass
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
    
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


class AccountsViewsSignupTest(AccountsViewsTest):
    """signup_viewへのテストクラス"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.signup_url = reverse_lazy('account_signup')
        cls.email_verification_sent_url = reverse_lazy('account_email_verification_sent')

    def test_signup_success(self):
        """サインアップが成功することを検証"""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

        params = {
            'email': 'dummy@example.com',
            'password1': os.getenv('TESTUSER_PASSWORD'),
            'password2': os.getenv('TESTUSER_PASSWORD'),
        }
        response = self.client.post(self.signup_url, params)
        # サインアップに成功し、メールアドレス検証に遷移することを確認
        self.assertRedirects(response, self.email_verification_sent_url)
    
    def test_signup_failure(self):
        """サインアップが失敗することを検証"""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

        params = {
            'email': 'dummy@example.com',
            'password1': os.getenv('TESTUSER_PASSWORD'),
            'password2': 'dummypassword',
        }
        response = self.client.post(self.signup_url, params)
        # サインアップに失敗した際は再度サインアップページに戻ることを確認
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

class AccountsViewsLoginTest(AccountsViewsTest):
    """login_viewへのテストクラス"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.login_url = reverse_lazy('account_login')
        cls.portfolio_index_url = reverse_lazy('portfolio:index')

    def test_login_success(self):
        """ログインが成功することを検証"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        # ログイン用のユーザ作成
        self.create_user()

        params = {
            'login': 'dummy@example.com',
            'password': os.getenv('TESTUSER_PASSWORD'),
        }
        response = self.client.post(self.login_url, params)

        # ログインに成功し、Portfolioのトップページへ遷移することを確認
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.portfolio_index_url)

    def test_login_failure(self):
        """ログインが失敗することを検証"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

        params = {
            'login': 'dummy@example.com',
            'password': 'dummypassword',
        }
        response = self.client.post(self.login_url, params)

        # ログインに失敗した際は再度ログインページに戻ることを確認
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
