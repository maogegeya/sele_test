# coding: utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com/")
a = driver.find_element_by_xpath(".//*[@id='kw']").send_keys(u"中国")
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='kw']").click()
time.sleep(1)
# 获取百度输入框的匹配词
b = driver.find_elements_by_class_name("bdsug-overflow")
for i in b:
    print(i.get_attribute("data-key"))
# 点击其中一个匹配词（从0开始计数）
if len(b)>=1:
    b[1].click()
    print(driver.current_window_handle)
else:
    print("未获取到匹配的词")
