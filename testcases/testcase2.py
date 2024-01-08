"""
通过该方法无法正确的获取到验证码的图片，所以在网上找了解决方法，还好有大佬分享了可用的解决方法！！！详情见testcase3
"""
import time

from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By


def test1():
    browser=webdriver.Chrome()
    browser.get("https://www.qb5.ch/login.php")
    browser.maximize_window()

    t=time.time()
    picture_name1=str(t)+'.png'
    browser.save_screenshot(picture_name1)
    ce=browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/form/fieldset/p[3]/img")
    print(ce.location)
    left=ce.location['x']
    top=ce.location['y']
    right=ce.size['width']+left
    height=ce.size['height']+top

    im=Image.open(picture_name1)
    # 抠图
    img=im.crop((left,top,right,height))

    t=time.time()
    picture_name2=str(t)+'.png'

    img.save(picture_name2)
    browser.close()