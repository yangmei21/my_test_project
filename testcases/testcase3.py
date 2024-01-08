"""
将验证码图片保存并且识别
参考实现：https://blog.csdn.net/weixin_45541762/article/details/115526509
"""
from PIL import Image
from selenium import webdriver
import time
import pytesseract

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test1():
    browser=webdriver.Chrome()
    browser.get('https://www.qb5.ch/login.php')
    browser.maximize_window()
    t = time.time()
    picture_name2 = str(t) + '.png'
    WebDriverWait(browser, 10, 0.5).until(lambda el: browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/form/fieldset/p[3]/img'))
    browser.find_element(By.XPATH,'/html/body/div[3]/div[1]/form/fieldset/p[3]/img').screenshot(picture_name2)
    time.sleep(2)
    browser.close()

def test2():
    imagel=Image.open('1704204049.1900313.png')
    str=pytesseract.image_to_string(imagel)
    print(str)