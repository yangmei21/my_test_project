import time
from selenium import webdriver
from util.log import Logger

logger = Logger(logger='TestMylog').getlog()


class TestMylog(object):
    def print_log(self):
        driver = webdriver.Firefox()
        # logger.info("打开浏览器")
        driver.maximize_window()
        logger.info("最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        logger.info("打开百度首页。")
        time.sleep(1)
        logger.info("暂停一秒。")
        driver.quit()
        logger.info("关闭并退出浏览器。")


testlog = TestMylog()
testlog.print_log()
