import pytest
import xlrd
import openpyxl


def test_get_data():
    filename = 'data.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    # 读取数据
    for row in sheet.iter_rows():
        for cell in row:
            print(cell.value)


@pytest.mark.parametrize('name', test_get_data())
def test1(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv', 'test_excel.py'])
