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


class TestFoodmanag(object):

    def setup_method(self):
        self.login = TestAdminLogin
        print('调用loginadmin--setup')

    @pytest.mark.dependency(depends=['admin_login'], scope='module')
    def test_add_foodshop_basic(self):
        '''
        添加美食成功
        '''
        food_name = 'test1'
        food_detail = 'test2'
        food_add = 'test3'
        food_phone = 'test4'

        # 点击关闭弹框
        sleep(2)
        self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
        sleep(2)
        # 点击发布信息管理
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
        sleep(2)
        # 点击美食管理
        self.login.driver.find_element(By.LINK_TEXT,
                                       '美食管理').click()

        sleep(2)
        # 获取列表数据总数
        # ！！！
        # 定位包含总数据条数信息的元素
        food_total = util.get_total(self.login.driver, '.ant-pagination-total-text')
        print("列表总数为：", food_total)

        # 点击新建
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button').click()
        # 页面最大化
        # self.login.driver.find_element(By.XPATH,
        #                                '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()

        # 定位商家类型选择框,点击展开
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[1]/nz-form-control/div/div/nz-select').click()

        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-2"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "火锅":
                option.click()
                break
        sleep(2)

        # 上传商家图片
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic8.png")

        # 上传商家缩略图
        upload_element = self.login.driver.find_element(By.XPATH,
                                                        '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[3]/nz-form-control/div/div/div[1]/nz-upload/div/div/input')
        upload_element.send_keys(r"F:\picture\test\pic9.png")
        # upload_element.send_keys(Keys.RETURN)

        # 填写商家店名称
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[4]/nz-form-control/div/div/input').send_keys(
            food_name)
        # 填写商家介绍
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[5]/nz-form-control/div/div/textarea').send_keys(
            food_detail)
        # 填写商家地址
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[6]/nz-form-control/div/div/input').send_keys(
            food_add)
        # 填写联系电话
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[9]/nz-form-control/div/div/input').send_keys(
            food_phone)
        sleep(5)
        # 选择开放起始时间
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[7]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "8:30")
        # 选择开放截至时间
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[8]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "23:00")
        sleep(2)

        # 定义套餐字段内容
        pack_name = '1'
        pack_datil = '2'
        pack_price = '3'
        ngredients = '4'
        order = '5'
        # 点击新增套餐
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[10]/nz-form-control/div/div/div[1]/a/span').click()
        sleep(5)
        # 最大化[无法定位最大化就不最大化了]
        # self.login.driver.find_element(By.XPATH,
        #                                '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
        # 上传套餐图片
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic8.png")
        sleep(2)
        # 套餐名称
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/input').send_keys(
            pack_name)
        # 套餐描述
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[3]/nz-form-control/div/div/input').send_keys(
            pack_datil)
        # 套餐价格
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div/div/input').send_keys(
            pack_price)
        # 主料
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[5]/nz-form-control/div/div/input').send_keys(
            ngredients)
        # 套餐排序
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[6]/nz-form-control/div/div/input').send_keys(
            order)
        sleep(3)
        # 点击确定按钮
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[3]/button[1]').click()

        # 定义菜品字段内容
        Dishes_name = '1'
        Dishes_datil = '2'
        Dishes_price = '3'
        Dishes_main = '4'
        Dishes_acc = '5'
        Dishes_order = '1'
        # 点击新建菜品
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[11]/nz-form-control/div/div/div[1]/a/span').click()
        # 展开分类
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select/nz-select-top-control').click()
        #  选择菜品分类
        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '/html/body/div[2]/div[5]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "主食":
                option.click()
                break
        sleep(2)
        # 上传菜品图片
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic8.png")
        # 填写菜品名称
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[3]/nz-form-control/div/div/input').send_keys(
            Dishes_name)
        # 填写菜品描述
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div/div/input').send_keys(
            Dishes_datil)
        # 填写菜品价格
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[5]/nz-form-control/div/div/input').send_keys(
            Dishes_price)

        # 点击菜品单位展开
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[6]/nz-form-control/div/div/nz-select/nz-select-top-control').click()
        #  选择菜品单位分类
        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '/html/body/div[2]/div[5]/div/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "盘":
                option.click()
                break
        sleep(2)
        # 填写主料
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[7]/nz-form-control/div/div/input').send_keys(
            Dishes_main)
        # 填写辅料
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[8]/nz-form-control/div/div/input').send_keys(
            Dishes_acc)
        # 选择荤素（单选框）
        # 荤：
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[9]/nz-form-control/div/div/nz-radio-group/label[1]/span[1]/input').click()
        # 素：
        # self.login.driver.find_element(By.XPATH,
        #                                '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[9]/nz-form-control/div/div/nz-radio-group/label[2]/span[1]/input').click()

        # 填写排序值
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[10]/nz-form-control/div/div/input').send_keys(
            Dishes_order)
        # 点击确定按钮
        self.login.driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/nz-modal-container/div/div/div[3]/button[1]').click()
        sleep(5)
        # 点击提交按钮
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept-manage-modal/div/form/nz-form-item[12]/nz-form-control/div/div/button[1]').click()
        sleep(1)
        # 刷新页面数据（页面刷新不行，我选择使用点击搜索来刷新！！！不是刷新不行，是变量传递的问题o(╥﹏╥)o）
        # self.login.driver.refresh()
        # self.login.driver.find_element(By.XPATH,'/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/nz-card/div/form/div/div[3]/button[1]').click()

        # 验证是否新增成功（与新增前获取的总数值进行对比）
        food_add_total = util.get_total(self.login.driver, '.ant-pagination-total-text')
        print("新增后列表总数为：", food_add_total)

        assert food_add_total == food_total + 1

        sleep(3)

    def teardowm_class(self):
        self.login.driver.quit()


if __name__ == '__main__':
    pytest.main(['test_food_manag.py'])
