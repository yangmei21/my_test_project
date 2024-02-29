"""
    获取页面失败时截图
"""

from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestLogin():
    def setup_class(self):
        url_login = 'https://passport.cnblogs.com/user/signin'
        self.driver = webdriver.Firefox()
        self.driver.get(url_login)
        self.driver.maximize_window()
        time.sleep(2)

    def test_01(self):
        try:
            self.driver.find_element(By.XPATH, '//input[@formcontrolname="username"]').send_keys('1154372391@qq.com')
            self.driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys('999999')
            self.driver.find_element(By.XPATH, "//button[@color='primary']").click()
            time.sleep(2)
            locator = ('ID', 'Ink_current_user')
            result = EC.text_to_be_present_in_element(locator, 'aajdfjdj')(self.driver)
            assert (result)
        except Exception as msg:
            print(u'异常问题%s' % msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
            raise

    def teardown_class(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main()
