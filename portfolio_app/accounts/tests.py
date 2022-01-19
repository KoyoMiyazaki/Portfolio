from django.test import LiveServerTestCase
from django.urls import reverse_lazy
import chromedriver_binary
from selenium.webdriver.chrome.webdriver import WebDriver
from .models import CustomUser

import time

class TestAccounts(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        # cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    # login/logoutについてのテスト
    def test_login_and_logout(self):
        self.selenium.implicitly_wait(10)
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        # ログイン画面に移ったことを確認
        self.assertEquals("ログイン | Portfolio", self.selenium.title)
        
        # 要素の初期化
        email_input = self.selenium.find_element_by_name("login")
        password_input = self.selenium.find_element_by_name("password")
        button_login = self.selenium.find_element_by_id('btn-login')

        # 各種入力
        email_input.send_keys('testuser@test.com')
        password_input.send_keys('!xHb5uJ2vr')
        button_login.click()

        # ログイン成功し、Portfolioトップページへ移ることを確認
        self.assertEquals("My Portfolio | Portfolio", self.selenium.title)

        # ログアウト後(ログアウトへGET後)、サインアップ画面へ移ることを確認
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_logout')))
        self.assertEquals("サインアップ | Portfolio", self.selenium.title)
    
    # signupについてのテスト
    def test_signup(self):
        self.selenium.implicitly_wait(10)
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_signup')))

        # サインアップ画面に移ったことを確認
        self.assertEquals("サインアップ | Portfolio", self.selenium.title)
        
        # 要素の初期化
        email_input = self.selenium.find_element_by_name("email")
        password1_input = self.selenium.find_element_by_name("password1")
        password2_input = self.selenium.find_element_by_name("password2")
        button_signup = self.selenium.find_element_by_id('btn-signup')

        # 各種入力
        email_input.send_keys('dummy@test.com')
        password1_input.send_keys('!xHb5uJ2vr')
        password2_input.send_keys('!xHb5uJ2vr')
        button_signup.click()

        # 入力後、メールアドレス検証画面へ移ることを確認
        self.assertEquals("メールアドレスを確認してください | Portfolio", self.selenium.title)

        # time.sleep(3)
        # ダミーユーザを削除
        # CustomUser.objects.get(email='dummy@test.com').delete()

    # password_resetについてのテスト
    def test_password_reset(self):
        self.selenium.implicitly_wait(10)
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_reset_password')))

        # パスワードリセット画面に移ったことを確認
        self.assertEquals("パスワードリセット | Portfolio", self.selenium.title)
        
        # 要素の初期化
        email_input = self.selenium.find_element_by_name("email")
        button_password_reset = self.selenium.find_element_by_id('btn-password-reset')

        # 各種入力
        email_input.send_keys('testuser@test.com')
        button_password_reset.click()

        self.selenium.implicitly_wait(10)
        # 入力後、パスワードリセットメール送信完了画面へ移ることを確認
        self.assertEquals("パスワードリセット用のメールを送信しました | Portfolio", self.selenium.title)
    