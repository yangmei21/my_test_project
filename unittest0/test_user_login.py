from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/user/login.html')
        self.driver.maximize_window()

    # 测试用户登录，用户名为空
    def test_user_login_username_empty(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        excepted = '手机号不能为空！'

        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == excepted

    # 测试用户登录，密码为空
    def test_user_login_pwd_empty(self):
        # 用户名为空
        username = '18890032513'
        pwd = ''
        excepted = '密码不能为空！'

        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == excepted

    # 测试用户登录，账号、密码错误
    def test_user_login_userpwd_error(self):
        # 用户名为空
        username = '18890032513'
        pwd = '989888'
        excepted = '手机号或密码错误！'

        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == excepted

    def test_user_login_right(self):
        # 正确登录
        username = '13039131599'
        pwd = '123456'
        expecttitle = '读书屋_原创小说网站'

        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        assert self.driver.title == expecttitle
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()