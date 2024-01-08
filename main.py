from testcases import testcase1, testcase2, testcase3
from util import util
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_login import TestAdminLogin
from testcases.basic.test_add_scenic import TestAddScenic
from testcases.basic.test_del_shopinfo import TestDelshopinfo
from testcases.basic.test_regibus import TestRegibuss

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # testcase1.test1()
    # testcase2.test1()
    # testcase3.test1()
    # testcase3.test2()
    # print(util.gen_random_str())

    # 调用util中获取验证码的方法并获取验证码
    # driver=webdriver.Chrome()
    # driver.get('https://www.qb5.ch/login.php')
    # driver.maximize_window()
    # print(util.get_code(driver,'/html/body/div[3]/div[1]/form/fieldset/p[3]/img'))

    # 调用注册用例
    # case01 = TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_register_right()

    # 调用登录用例
    # case02=TestUserLogin()  #实例化
    # case02.test_user_login_username_empty()
    # case02.test_user_login_pwd_empty()
    # case02.test_user_login_userpwd_error()
    # case02.test_user_login_right()

    # 调用管理员登录
    # case03=TestAdminLogin()
    # case03.test_admin_login_username_err()
    # case03.test_admin_login_right()

    # 调用添加景点(依赖登录，所以需要把登录的方法传过去)
    # login=TestAdminLogin()
    # login.test_admin_login_right()
    # case04=TestAddScenic(login)
    # case04.test_add_scenic_err()
    # case04.test_add_scenic_right()

    # 调用商家信息删除（依赖登录，也需要把登录加入）
    # login=TestAdminLogin()
    # login.test_admin_login_right()
    # case05=TestDelshopinfo(login)
    # # case05.del_cancel_shopinfo()
    # case05.del_succ_shopinfo()

    # # 调用商家注册（依赖登录，插入登录）
    login = TestAdminLogin()
    login.test_admin_login_right()
    case06=TestRegibuss(login)
    case06.test_regibus()