import openpyxl

def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append({
            "num": row[0],
            "pwd": row[1],
            "expc": row[2]
        })

    workbook.close()
    return data

def test_read_excel():
    file_path = "D://test_data//login_data.xlsx"
    excel_data = read_excel(file_path)

    for row in excel_data:
        print(f"账号: {row['num']}, 密码: {row['pwd']}, 期望结果: {row['expc']}")

if __name__ == "__main__":
    test_read_excel()
