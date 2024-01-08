from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/login/login-form')
        self.driver.maximize_window()

    # 判断用户名、密码错误登录
    def test_admin_login_username_err(self):
        username = 'admi'
        pwd = '123456'
        excpet = '登录失败，用户名密码错误或该账号已被禁用！'

        user = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="userName"]')
        user[0].send_keys(username)
        pw = self.driver.find_elements(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
        pw[0].send_keys(pwd)
        bt = self.driver.find_element(By.CSS_SELECTOR, 'button.ant-btn-primary')
        bt.click()

        loc=(By.XPATH,'//*[@id="cdk-overlay-0"]/nz-message-container/div/nz-message/div/div/div/span[2]')
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located(loc))
        msg=self.driver.find_element(*loc).text
        print(msg)
        assert msg == excpet
        sleep(2)
        self.driver.quit()   #一起调用时需要把quit关闭，并且下列输入时要先清空，调用clear事件

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
        assert self.driver.title == excpetitle
