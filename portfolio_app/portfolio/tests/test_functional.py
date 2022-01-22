from django.test import LiveServerTestCase
from django.urls import reverse_lazy
import chromedriver_binary
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

import os
import time
from dotenv import load_dotenv

load_dotenv()

class PortfolioFunctionalTest(LiveServerTestCase):
    """Portfolioトップページを検証する基底クラス"""

    # sleepの秒数
    SLEEP_SECONDS = 2

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        # options.add_argument('--headless')
        cls.selenium = WebDriver(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def login(self):
        """テスト用ユーザでログインを行う"""
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))
        
        # 要素の初期化
        email_input = self.selenium.find_element_by_name("login")
        password_input = self.selenium.find_element_by_name("password")
        button_login = self.selenium.find_element_by_id('btn-login')

        # 各種入力
        email_input.send_keys('testuser@test.com')
        password_input.send_keys(os.getenv('TESTUSER_PASSWORD'))
        button_login.click()

class NavbarFunctionalTest(PortfolioFunctionalTest):
    """ナビゲーションバーのテストクラス"""

    # テーマボタンのクリック回数
    TIMES_OF_THEME_CLICK = 2

    def test_menu_behavior(self):
        """メニューの挙動を検証する"""
        self.login()
        self.selenium.implicitly_wait(10)

        # Aboutボタンの検証
        about_link = self.selenium.find_element_by_xpath("//a[@href='#about']")
        self.assertEqual(about_link.text, 'About')
        about_link.click()
        time.sleep(self.SLEEP_SECONDS)

        # Skillsボタンの検証
        skills_link = self.selenium.find_element_by_xpath("//a[@href='#skills']")
        self.assertEqual(skills_link.text, 'Skills')
        skills_link.click()
        time.sleep(self.SLEEP_SECONDS)

        # Portfolioボタンの検証
        portfolio_link = self.selenium.find_element_by_xpath("//a[@href='#portfolio']")
        self.assertEqual(portfolio_link.text, 'Portfolio')
        portfolio_link.click()
        time.sleep(self.SLEEP_SECONDS)

        # Homeボタンの検証
        home_link = self.selenium.find_element_by_xpath("//a[@href='#home']")
        self.assertEqual(home_link.text, 'Home')
        home_link.click()
        time.sleep(self.SLEEP_SECONDS)

        # テーマボタンの検証
        for i in range(self.TIMES_OF_THEME_CLICK):
            theme_button = self.selenium.find_element_by_id('theme-button')
            if i % 2 == 0:
                self.assertEqual(theme_button.get_attribute('class'), "uil uil-moon change-theme")
            else:
                self.assertEqual(theme_button.get_attribute('class'), "uil uil-moon change-theme uil-sun")
            theme_button.click()
            time.sleep(self.SLEEP_SECONDS)

class MainContentFunctionalTest(PortfolioFunctionalTest):
    """メインコンテンツのテストクラス"""

    def test_should_exist_content(self):
        """コンテンツの存在を検証する"""
        self.login()
        self.selenium.implicitly_wait(10)

        # Homeコンテンツの検証
        home_content = self.selenium.find_element_by_id('home')
        self.assertNotEqual(home_content.text, "")

        # Aboutコンテンツの検証
        about_content = self.selenium.find_element_by_id('about')
        self.assertNotEqual(about_content.text, "")

        # Skillsコンテンツの検証
        skills_content = self.selenium.find_element_by_id('skills')
        self.assertNotEqual(skills_content.text, "")

        # Portfolioコンテンツの検証
        portfolio_content = self.selenium.find_element_by_id('portfolio')
        self.assertNotEqual(portfolio_content.text, "")