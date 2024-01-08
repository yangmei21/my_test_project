# 参数化
import pytest

# 列表
data=['123','66625']
@pytest.mark.parametrize('pwd',data)
def test1(pwd):
    print(pwd)

# 元组
data2=[
    (1,2,3888),
    (2,63,695)
]
@pytest.mark.parametrize('a,b,c',data2)
def test2(a,b,c):
    print(a,b,c)

# 字典
data3=(
    {
        'user':'wang',
        'pwd':'9999'
    },
    {
        'age':32,
        'email':'158@163.com'
    }
)
@pytest.mark.parametrize('dic',data3)
def test3(dic):
    print(dic)