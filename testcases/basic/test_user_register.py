from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/user/register.html')
        self.driver.maximize_window()

    # 测试验证码登录错误
    def test_register_code_error(self):
        username = '13039131599'
        pwd = '123456'
        code = '6666'
        expect = '验证码错误！'

        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'TxtChkCode').send_keys(code)
        self.driver.find_element(By.ID, 'btnRegister').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == expect

        sleep(3)

    # 测试注册成功
    def test_register_right(self):
        username = '13039131598'
        pwd = '123456'
        # 验证码自动获取
        code = ''
        expecttitle = '读书屋_原创小说网站'
        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(pwd)
        self.driver.find_element(By.ID, 'TxtChkCode').clear()
        code = util.get_code(self.driver, '//*[@id="chkd"]')
        self.driver.find_element(By.ID, 'TxtChkCode').send_keys(code)
        self.driver.find_element(By.ID, 'btnRegister').click()
        sleep(2)
        url = self.driver.title
        assert url == expecttitle
        self.driver.quit()