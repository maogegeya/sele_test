# coding: utf-8
from selenium import webdriver
import time
url = "file:///C:/Users/Solar Mao/Desktop/testalert.html"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)
driver.find_element_by_id("prompt").click()
time.sleep(3)
t = driver.switch_to_alert()
# 打印警告框文本内容
print(t.text)
# 点警告框确认按钮
# t.accept()
# 点关闭警告框按钮
# t.dismiss()
# 输入文本内容
t.send_keys("Hello Selenium2")
t.accept()