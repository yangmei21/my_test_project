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

'''
商家发布页面功能测试用例 [写到第二个提示被拒绝了写不下去了。]
进入商家发布页：test_goto_publish_buss
查询商家发布信息：test_search_publish_buss
审核商家发布信息：test_audit_publish_buss
删除商家发布信息：test_del_publish_buss

'''


class Test_buss_publish(object):
    def setup_class(self):
        self.login = TestAdminLogin
        print("调用管理员登录")

    @pytest.mark.dependency(depends=['admin_login'], scope='module')
    def test_goto_publish_buss(self):
        '''
        这是判断是否进入了商家发布页
        :return:
        '''
        # 点击关闭弹框
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        # 点击信息审核管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[4]/div[1]/span[1]').click()
        # 点击商家商家信息审核
        self.login.driver.find_element(By.LINK_TEXT, '商家发布信息审核').click()
        sleep(1)
        present_url = self.login.driver.current_url
        assert present_url == 'http://202.111.177.155:8081/manager/static/ng-ant-admin/index.html#/default/audit/audit'
        print('\n成功进入商家发布页')

    def test_audit_publish_buss(self):
        '''
        这是审核操作
        :return:
        '''
        sleep(2)
        status = self.login.driver.find_element(By.XPATH,
                                                '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[2]/app-tree-table/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[4]')
        print('\n该数据审核状态为：', status.text)

        # 进入审核界面
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[2]/app-tree-table/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[7]/span[1]').click()
        # 界面最大化[关注页面是否刷新操作，因为前面的步骤导致元素xpath会不一致，所以要复现前面的步骤才能定位到最新的xpath]
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()

        sleep(3)

    def norun_test_search_publish_buss(self):
        '''
        这是查询
        :return:
        '''
        # 获取列表第一条数据标题（存在的数据）
        self.login.driver.refresh()
        sleep(1)
        exist_title = self.login.driver.find_element(By.XPATH,
                                                     '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[2]/app-tree-table/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[1]/span')
        print('\n存在的标题名称为：', exist_title.text)
        #  获取存在第一条数据的分类（一定存在的）
        exist_classify = self.login.driver.find_element(By.XPATH,
                                                        '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[2]/app-tree-table/nz-table/nz-spin/div/div/nz-table-inner-scroll/div/table/tbody/tr[2]/td[4]')
        print('存在的分类名称为：', exist_classify.text)

        # 输入标题到搜索框
        self.login.driver.find_element(By.XPATH, '//input[@placeholder="请输入名称"]').send_keys(
            exist_title.text)
        # 展开分类
        self.login.driver.find_element(By.XPATH,
                                       "/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/nz-card/div/form/div/div[2]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control").click()
        # 输入选择分类到框中
        sleep(1)

        options = WebDriverWait(self.login.driver, 5).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-5"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == exist_classify.text:
                option.click()
                break
        sleep(2)

        # 点击搜索按钮
        self.login.driver.find_element(By.CLASS_NAME, 'ant-btn-primary').click()

        # 判断是否查到数据【判断列表是否有数据】
        research_total = util.get_total(self.login.driver, '.ant-pagination-total-text')
        print("列表查询到的数为：", research_total)
        # 断言(好像不太严谨，但是目前方法准测是是商家名称唯一，存在一条数据)
        assert research_total == 1
        print('根据名称与审核状态能够正确查询！！！查询数为', research_total)

    def teardown(self):
        self.login.driver.quit()
        print("已执行完所有用例，退出浏览器！！！")


if __name__ == '__main__':
    pytest.main(['-vs', 'test_buss_publish.py'])
