from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from util.log import Logger

logging = Logger(logger='TestUserLogin').getlog()


class TestUserLogin(object):

    def setup_class(self):
        self.driver = webdriver.Firefox()
        sleep(2)
        self.driver.get('http://novel.hctestedu.com/user/login.html')
        self.driver.maximize_window()
        # testlog=TestUserLogin()
        logging.info('打开浏览器')

    login_data = [
        ('', '123456', '手机号不能为空！'),
        ('18890032513', '', '密码不能为空！'),
        ('18890032513', '989888', '手机号或密码错误！')
    ]

    @pytest.mark.parametrize('username,pwd,excepted', login_data)
    def test_uesr_err_login(self, username, pwd, excepted):
        '''
        验证登录异常情况（异常用例）
        :param username: username
        :param pwd: pwd
        :param excepted: excepted
        :return: err
        '''
        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        logging.debug("输入账号：%s",username)
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        logging.debug("输入密码：%s", pwd)
        self.driver.find_element(By.ID, 'btnLogin').click()
        logging.debug("点击登录按钮")
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == excepted, '验证失败，请检查'

    def test_uesr_ok_login(self):
        '''
        验证正常登录用例：正确的用户名及密码
        :return:
        '''
        self.driver.find_element(By.ID, 'txtUName').clear()
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
