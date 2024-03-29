# BasePage类：定义查找元素等一些基本方法
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    
    def type_text(self,text,*loc):
        self.find_element(*loc).send_keys(text)

    def click(self,*loc):
        self.find_element(*loc).click()

    def clear(self,*loc):
        self.find_element(*loc).clear()

    def get_title(self):
        return self.driver.title

    def err_mess(self,*loc):
        err=self.driver.find_element(*loc).text
        return err
