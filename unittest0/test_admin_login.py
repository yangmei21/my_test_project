from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class TestAdminLogin(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form')
        self.driver.maximize_window()

    # 管理员正确登录
    def test_admin_login_right(self):
        username = 'admin'
        pwd = '123456'
        excpetitle = '工作台'

        user = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
        user[0].send_keys(username)
        pw = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        pw[0].send_keys(pwd)
        bt = self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
        bt.click()

        sleep(2)
        # assert self.driver.title == excpetitle
        self.assertEqual(self.driver.title, excpetitle)
