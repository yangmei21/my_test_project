import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

from pom_test.userLoginPage import UserLoginPage
from pom_test.BasePage import BasePage


class TestUserLogin(object):
    login_data = [
        ('18890032513', '', '密码不能为空！'),
        ('', '123456', '手机号不能为空！'),
        ('18890032513', '989888', '手机号或密码错误！')
    ]

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.loginPage = UserLoginPage(self.driver)
        self.loginPage.goto_login_page()

    # 测试用户登录
    @pytest.mark.parametrize('username,pwd,expected', login_data)
    def test_user_login(self, username, pwd, expected):

        # 输入用户名
        self.loginPage.input_username(username)
        # 输入密码
        self.loginPage.input_pwd(pwd)
        # 点击登录
        self.loginPage.click_login_btn()
        sleep(2)

        # 验证
        assert expected == self.driver.find_element(By.ID, 'LabErr').text

    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv', 'testUserLogin.py'])
