from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestUserLogin(object):

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/user/login.html')
        self.driver.maximize_window()

    login_data = [
        ('', '123456', '手机号不能为空！'),
        ('18890032513', '', '密码不能为空！'),
        ('18890032513', '989888', '手机号或密码错误！')
    ]

    @pytest.mark.parametrize('username,pwd,excepted', login_data)
    def test_uesr_err_login(self, username, pwd, excepted):
        self.driver.find_element(By.ID,'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)

        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)

        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == excepted

    def test_uesr_ok_login(self):
        self.driver.find_element(By.ID,'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys('13039131596')

        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys('123456')

        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)

        assert self.driver.title == '读书屋_原创小说网站'

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_userlogin.py'])
