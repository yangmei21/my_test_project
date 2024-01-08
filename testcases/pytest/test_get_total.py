# 测试工具类中的调用获取总数
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
import re
import pytest


from testcases.pytest.test_login import TestAdminLogin
from util.get_total import get_total
from util import util
class TestAddScenic(object):

    def setup_method(self):
        self.login = TestAdminLogin
        print('调用loginadmin--setup')

    @pytest.mark.dependency(depends=['admin_login'], scope='module')
    def test_add_scenic_right(self):
        # 点击关闭弹框
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        sleep(1)
        # 点击发布信息管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
        sleep(2)
        # 点击景点管理
        self.login.driver.find_element(By.LINK_TEXT,
                                       '景点管理').click()

        sleep(2)
        # 调用获取页面总数(单独的方法）
        total1=get_total(self.login.driver,'.ant-pagination-total-text')
        print('方法1获取：',total1)
        # 或者：（util文件中包含多个方法，所以要单一引用）
        total2=util.get_total(self.login.driver,'.ant-pagination-total-text')
        print('方法2获取：',total2)

if __name__ == '__main__':
    pytest.main(['test_get_total.py'])