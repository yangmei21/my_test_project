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
from util import util


class TestAddLine(object):

    def setup_class(self):
        self.login = TestAdminLogin
        print('调用loginadmin--setup')

    @pytest.mark.dependency(depends=['admin_login'], scope='module')
    def test_add_line(self):
        '''
        验证是否可以正常新增线路
        :return:
        '''
        line_name = 'test腾格里沙漠五湖穿越'
        line_introduce = '常规路线】天鹅湖一乌兰湖一苏海图湖一太阳湖一月亮湖一梦想沙漠公路.格里沙漠，雄踞内蒙古阿拉善高原的东南部，面积3.87万平方公里，是我国第四大沙漠。蒙古语中，“腾格里”是“天”的意思，形容这片沙漠“像天一样高远、辽阔”。当地牧民说：“登上腾格里，离天三尺三”，他们对腾格里沙漠万分敬畏，却又十分依恋，从古至今，蒙古族牧民在腾格里沙漠的绿洲上建立家园，他们在绿洲之间来往迁徙。腾格里沙漠还是许多鸟类和走兽的栖息地，人类和万物共同在这里完成着生命的繁衍。'

        # 点击关闭弹框
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        sleep(2)
        # 点击发布信息管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
        sleep(2)
        # 点击线路推荐
        self.login.driver.find_element(By.LINK_TEXT,
                                       '线路推荐').click()

        sleep(2)
        # 获取列表总数
        line_total = util.get_total(self.login.driver, '.ant-pagination-total-text')
        print("列表总数为：", line_total)

        # 点击新建按钮
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button').click()
        sleep(2)
        # 点击页面最大化
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
        # 点击线路类型，展开列表
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input').click()
        # 定位并选择类型
        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "景点自驾路线":
                option.click()
                break
        # 上传线路图片
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic8.png")
        # 上传线路缩略图
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[3]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic9.png")
        # 填写线路名称
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div/div/input').send_keys(
            line_name)
        # # 填写线路介绍
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[5]/nz-form-control/div/div/textarea').send_keys(
            line_introduce)

        # 点击所在城市，展开城市列表
        dropdown = self.login.driver.find_element(By.XPATH,
                                                  '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[6]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input')
        dropdown.click()

        # 定位并选择城市,按照之前的方法获取不了所以列表，因为内容过多，求助了chat!!!他写了下面的方法，操作键盘向下选择，我真的不得不说人工智能牛啊啊
        # 不过这我要获取所有城市列表才行；感觉如果时正式环境中，可以查看数据库列表查看

        # 模拟按键操作，可以使用循环模拟多次按下 Arrow Down 键
        for _ in range(2):  # 模拟按下 5 次 Arrow Down 键；选择第五个
            dropdown.send_keys(Keys.ARROW_DOWN)

        # 模拟按键 Enter 选中项
        dropdown.send_keys(Keys.ENTER)

        # 点击确定按钮
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[3]/button[1]').click()
        sleep(2)

        self.login.driver.refresh()

        # 获取新增后的列表数
        add_total = util.get_total(self.login.driver, '.ant-pagination-total-text')
        print('新增后的列表总数', add_total)
        # 断言验证是否新增成功
        assert add_total == line_total + 1
        sleep(3)

    def teardown_class(self):
        self.login.driver.quit()
        print('执行结束！！！teardown--关闭浏览器')


if __name__ == '__main__':
    pytest.main(['-sv', 'test_add_line.py'])
