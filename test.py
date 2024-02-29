import logging
import pytest
# 配置日志输出到控制台和文件
logging.basicConfig(
    filename='test.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


def test_case_1():
    logging.info("开始执行测试用例1")

    try:
        # 一些测试代码
        result = 5 / 0  # 引发一个除零异常
    except Exception as e:
        logging.error(f'测试用例1执行失败: {e}')

    logging.info("结束测试用例1")


def test_case_2():
    logging.info("开始执行测试用例2")

    try:
        # 一些测试代码
        assert 2 + 2 == 5, "断言失败"  # 引发一个断言错误
    except AssertionError as e:
        logging.error(f'测试用例2执行失败: {e}')

    logging.info("结束测试用例2")


if __name__ == "__main__":
    logging.info("开始测试")

    test_case_1()
    test_case_2()

    logging.info("测试结束")
