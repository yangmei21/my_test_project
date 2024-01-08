"""
模块级 (setup_module/teardown_module) 开始于模块始未，全局的
函数级(setup_function/teardown_function) 只对函数用例生效 (不在类中)
类级 (setup_class/teardown_class) 只在类中前后运行一次(在类中)
方法级(setup_method/teardown_method) 开始于方法始未(在类中)
    类里面的 (setup/teardown) 运行在调用方法的前后
"""

import pytest

class Testcase01(object):
    @classmethod
    def setup_class(cls):
        print("类的setup")

    @classmethod
    def teardown_class(self):
        print('类的teardown')

    @pytest.mark.run(order=1)
    def test1(self):
        print('类的test1111111111111')

    @pytest.mark.run(order=2)
    def test2(self):
        print('类的test2222222222222')

# def setup_module():
#     print('模块setup_module')
#
#
# def teardown_module():
#     print('模块teardown_module')
#
#
# def setup_function():
#     print('函数setup_module')
#
#
# def teardown_function():
#     print('函数teardowm')

#
# def test1():
#     print('11test11')
#
#
# def test2():
#     print('22test22')


if __name__ == '__main__':
    pytest.main(['test02.py', '-s'])
