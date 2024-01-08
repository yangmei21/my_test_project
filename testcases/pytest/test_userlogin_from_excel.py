# 传空值无法正确执行（未解决）
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import openpyxl
from data import read_excel


class TestUserLogin(object):
    def read_excel(file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append({
                "username": row[0],
                "password": row[1],
                "expected_result": row[2]
            })

        workbook.close()
        return data

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/user/login.html')
        self.driver.maximize_window()

    @pytest.mark.parametrize('test_data', read_excel("D://test_data//login_data.xlsx"))
    def test_uesr_err_login(self, test_data):
        self.driver.find_element(By.ID, 'txtUName').clear()
        self.driver.find_element(By.ID, 'txtUName').send_keys(test_data['username'])

        self.driver.find_element(By.ID, 'txtPassword').clear()
        self.driver.find_element(By.ID, 'txtPassword').send_keys(test_data['password'])

        self.driver.find_element(By.ID, 'btnLogin').click()
        sleep(2)
        err = self.driver.find_element(By.ID, 'LabErr').text
        assert err == test_data['expected_result']

    def test_uesr_ok_login(self):
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
