from time import sleep

from selenium.webdriver.common.by import By

from pom_test.BasePage import BasePage

class UserLoginPage(BasePage):
    username_input=(By.ID,'txtUName')
    pwd_input=(By.ID,'txtPassword')
    login_btn=(By.ID,'btnLogin')
    err_me=(By.ID,'LabErr')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def goto_login_page(self):
        self.driver.get('http://novel.hctestedu.com/user/login.html')
        self.driver.maximize_window()

    def input_username(self,username):
        self.clear(*self.username_input)
        self.type_text(username,*self.username_input)

    def input_pwd(self,pwd):
        self.clear(*self.pwd_input)
        self.type_text(pwd,*self.pwd_input)

    def click_login_btn(self):
        self.click(*self.login_btn)
        sleep(1)

    def err_mess(self):
        self.err_mess(*self.err_me)
        sleep(1)



