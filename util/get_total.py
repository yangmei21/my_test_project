# 获取页面总数
from selenium.webdriver.common.by import By


def get_total(driver,id):
    # 获取列表数据总数
    # ！！！
    # 定位包含总数据条数信息的元素
    total_records_element = driver.find_element(By.CSS_SELECTOR,id)

    # 获取元素文本信息
    if total_records_element:
        total_records_text = total_records_element.text
        # 从文本中解析出数字
        # 格式为：’1-10 共 15 条‘，需要获取其中的15
        total_records = int(total_records_text.split('共')[-1].split('条')[0].strip())
        return total_records
        print("新增前总数据条数：", total_records)
    else:
        print("未获取到总数据提条数")
        return False