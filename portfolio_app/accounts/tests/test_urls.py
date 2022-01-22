from django.test import TestCase
from django.urls import reverse_lazy, resolve
from allauth.account import views

class AccountsUrlsTest(TestCase):

    def test_signup_url(self):
        """accounts/signup/ のURLテスト"""
        url = reverse_lazy('account_signup')
        self.assertEqual(resolve(url).func, views.signup)
    
    def test_login_url(self):
        """accounts/login/ のURLテスト"""
        url = reverse_lazy('account_login')
        self.assertEqual(resolve(url).func, views.login)
    
    def test_logout_url(self):
        """accounts/logout/ のURLテスト"""
        url = reverse_lazy('account_logout')
        self.assertEqual(resolve(url).func, views.logout)
    
    def test_change_password_url(self):
        """accounts/password/change/ のURLテスト"""
        url = reverse_lazy('account_change_password')
        self.assertEqual(resolve(url).func, views.password_change)
    
    def test_set_password_url(self):
        """accounts/password/set/ のURLテスト"""
        url = reverse_lazy('account_set_password')
        self.assertEqual(resolve(url).func, views.password_set)
    
    def test_inactive_url(self):
        """accounts/inactive/ のURLテスト"""
        url = reverse_lazy('account_inactive')
        self.assertEqual(resolve(url).func, views.account_inactive)

    def test_email_url(self):
        """accounts/email/ のURLテスト"""
        url = reverse_lazy('account_email')
        self.assertEqual(resolve(url).func, views.email)

    def test_email_verification_sent_url(self):
        """accounts/confirm-email/ のURLテスト"""
        url = reverse_lazy('account_email_verification_sent')
        self.assertEqual(resolve(url).func, views.email_verification_sent)

    def test_confirm_email_url(self):
        """accounts/confirm-email/[key]/ のURLテスト"""
        url = reverse_lazy('account_confirm_email', args=[1234])
        self.assertEqual(resolve(url).func, views.confirm_email)
    
    def test_reset_password_url(self):
        """accounts/password/reset/ のURLテスト"""
        url = reverse_lazy('account_reset_password')
        self.assertEqual(resolve(url).func, views.password_reset)
    
    def test_reset_password_done_url(self):
        """accounts/password/reset/done/ のURLテスト"""
        url = reverse_lazy('account_reset_password_done')
        self.assertEqual(resolve(url).func, views.password_reset_done)

    def test_reset_password_from_key_url(self):
        """accounts/password/reset/key/[uidb36]/ のURLテスト"""
        url = reverse_lazy('account_reset_password_from_key', kwargs={'uidb36': 'test', 'key': 1})
        self.assertEqual(resolve(url).func, views.password_reset_from_key)

    def test_reset_password_from_key_done_url(self):
        """accounts/password/reset/key/done/ のURLテスト"""
        url = reverse_lazy('account_reset_password_from_key_done')
        self.assertEqual(resolve(url).func, views.password_reset_from_key_done)