import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestUserRegister(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form')
        cls.driver.maximize_window()

        # 失败登录

    def test_admin_login1_username_err(self):
        username = 'admi'
        pwd = '123456'
        excpet = '登录失败，用户名密码错误或该账号已被禁用！'

        user = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
        user[0].send_keys(username)
        pw = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        pw[0].send_keys(pwd)
        bt = self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
        bt.click()

        loc = (By.XPATH, '//*[@id="cdk-overlay-0"]/nz-message-container/div/nz-message/div/div/div/span[2]')
        WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located(loc))
        msg = self.driver.find_element(*loc).text
        print(msg)
        # assert msg == excpet
        self.assertEqual(excpet, msg)
        sleep(2)

    # 正确登录
    def test_admin_login2_right(self):
        username = 'admin'
        pwd = '123456'
        excpetitle = '工作台'


        sleep(2)
        user = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
        user[0].send_keys(username)
        pw = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        # sleep(2)
        pw[0].send_keys(pwd)

        bt = self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
        bt.click()

        sleep(2)
        # assert self.driver.title == excpetitle
        self.assertEqual(excpetitle, self.driver.title)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
