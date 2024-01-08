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


class TestAddScenic(object):

    def setup_method(self):
        self.login = TestAdminLogin
        print('调用loginadmin--setup')

    # 测试添加景区失败，图片封面图为空
    # @pytest.mark.dependency(depends=['admin_login'], scope='module')
    # def test_add_scenic_err(self):
    #
    #     excpet = '请上传景点图片或景点缩略图！'
    #     # 点击关闭弹框
    #     self.login.driver.find_element(By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button').click()
    #     sleep(1)
    #
    #     # 点击发布信息管理
    #     self.login.driver.find_element(By.XPATH,
    #                                    '//*[@id="menuNav"]/div[1]/app-side-nav/div/div[2]/app-nav-bar/ul/li[3]/div[1]/span[1]').click()
    #     sleep(2)
    #     # 点击景点管理
    #     self.login.driver.find_element(By.LINK_TEXT,
    #                                    '景点管理').click()
    #     sleep(1)
    #
    #     # 点击新建
    #     self.login.driver.find_element(By.XPATH,
    #                                    '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button/span').click()
    #     # 页面最大化
    #     self.login.driver.find_element(By.XPATH,
    #                                    '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
    #     # 定位分类选择框,点击展开
    #     self.login.driver.find_element(By.XPATH,
    #                                    '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select').click()
    #
    #     options = WebDriverWait(self.login.driver, 10).until(
    #         EC.visibility_of_all_elements_located((By.XPATH,
    #                                                '//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item/div'))
    #     )
    #     # 定位并选择自己想要勾选的分类
    #     for option in options:
    #         if option.text == "温泉":
    #             option.click()
    #             break
    #     # self.login.driver.find_element(By.XPATH,'//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[6]/div').click()
    #     sleep(2)
    #     # 点击确认按钮
    #     self.login.driver.find_element(By.XPATH,
    #                                    '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[3]/button[1]').click()
    #
    #     loc = (By.XPATH, '//*[@id="cdk-overlay-4"]/nz-message-container/div/nz-message/div/div/div/span[2]')
    #     WebDriverWait(self.login.driver, 20, 0.5).until(EC.visibility_of_element_located(loc))
    #     msg = self.login.driver.find_element(*loc).text
    #     print(msg)
    #     assert msg == excpet
    #     # self.login.driver.quit()

    @pytest.mark.dependency(depends=['admin_login'], scope='module')
    def test_add_scenic_right(self):
        '''添加景区成功'''
        scen_name = '周庄镇'
        scen_detail = '周庄，是一座江南小镇，有"中国第一水乡"之誉，是国家首批5A级景区。周庄始建于1086年(北宋元佑元年)，因邑人周迪功先生捐地修全福寺而得名。春秋时为吴王少子摇的封地，名为贞丰里。'
        scen_add = '江苏省苏州市昆山市周庄镇全福路43号'
        scen_phone = '4008282900'
        excpet = '必填项'
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
        # 获取列表数据总数
        # ！！！
        # 定位包含总数据条数信息的元素
        total_records_element = self.login.driver.find_element(By.CSS_SELECTOR,
                                                               '.ant-pagination-total-text')

        # 获取元素文本信息
        if total_records_element:
            total_records_text = total_records_element.text
            # 从文本中解析出数字
            # 格式为：’1-10 共 15 条‘，需要获取其中的15
            total_records = int(total_records_text.split('共')[-1].split('条')[0].strip())
            print("新增前总数据条数：", total_records)
        else:
            print("未获取到总数据提条数")

        # 点击新建
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/app-card-table-wrap/nz-card/div[1]/div/div[2]/div/div[1]/button/span').click()
        # 页面最大化
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/button/span/div/span[1]').click()
        # 定位分类选择框,点击展开
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[1]/nz-form-control/div/div/nz-select').click()

        options = WebDriverWait(self.login.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH,
                                                   '//*[@id="cdk-overlay-3"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item/div'))
        )

        # 定位并选择自己想要勾选的分类
        for option in options:
            if option.text == "古村古镇":
                option.click()
                break
        sleep(2)

        # 上传景点图片
        # upload_element = self.login.driver.find_element(By.XPATH,
        #                                                 '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div')
        # upload_element.send_keys(r"F:\picture\pic1.png")
        # upload_element.send_keys(Keys.RETURN)
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[2]/nz-form-control/div/div/div[1]/nz-upload/div/div/input').send_keys(
            r"F:\picture\test\pic7.png")

        # 上传景点缩略图
        upload_element = self.login.driver.find_element(By.XPATH,
                                                        '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[3]/nz-form-control/div/div/div[1]/nz-upload/div/div/input')
        upload_element.send_keys(r"F:\picture\test\pic7.png")
        # upload_element.send_keys(Keys.RETURN)

        # 填写景点名称
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[4]/nz-form-control/div/div/input[1]').send_keys(
            scen_name)
        # 填写风景介绍
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[5]/nz-form-control/div/div/textarea').send_keys(
            scen_detail)
        # 填写景点地址
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[6]/nz-form-control/div/div/input').send_keys(
            scen_add)
        # 填写联系电话
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[9]/nz-form-control/div/div/input').send_keys(
            scen_phone)
        sleep(5)
        # 选择开放起始时间
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[7]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "7:30")
        # 选择开放截至时间
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[2]/app-dept-manage-modal/form/nz-form-item[8]/nz-form-control/div/div/nz-time-picker/div/input').send_keys(
            "20:00")
        sleep(2)
        # 点击确认按钮
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="cdk-overlay-2"]/nz-modal-container/div/div/div[3]/button[1]').click()
        sleep(1)
        # 刷新页面数据（页面刷新不行，我选择使用点击搜索来刷新！！！不是刷新不行，是变量传递的问题o(╥﹏╥)o）
        # self.login.driver.refresh()
        # self.login.driver.find_element(By.XPATH,'/html/body/app-root/div/app-default/app-def-layout-content/nz-layout/nz-layout/nz-layout/nz-content/div/div/app-dept/div/nz-card/div/form/div/div[3]/button[1]').click()

        # 验证是否新增成功（与新增前获取的总数值进行对比）
        add_total_records_element = self.login.driver.find_element(By.CSS_SELECTOR,
                                                                   '.ant-pagination-total-text')

        # 获取元素文本信息
        if add_total_records_element:
            add_total_records_text = add_total_records_element.text
            # 从文本中解析出数字
            # 格式为：’1-10 共 15 条‘，需要获取其中的 15
            add_total_records = int(add_total_records_text.split('共')[-1].split('条')[0].strip())
            print("新增后总数据条数：", add_total_records)
        else:
            print("未获取到总数据提条数")

        assert add_total_records == total_records + 1

        sleep(3)
        # self.login.driver.quit()

    def teardowm_class(self):
        self.login.driver.quit()

if __name__ == '__main__':
    pytest.main(['test_addscen.py'])
