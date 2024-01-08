import pytest


class Test01(object):
    def test01(self):
        print('test01')


if __name__ == '__main__':
    # pytest.main(['test01.py'])
    pytest.main(['-s', '-vv', 'test01.py', '--alluredir', 'my_test_project/reports'])