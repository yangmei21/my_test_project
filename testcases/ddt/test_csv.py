import pytest
import csv

def test_get_data():
    with open('test.csv')as f:
        lst=csv.reader(f)
        my_data=[]
        for row in lst:
            my_data.extend(row)
        return my_data

@pytest.mark.parametrize('name',test_get_data())
def test01(name):
    print(name)

if __name__ == '__main__':
    pytest.main(['-sv','test_csv.py'])