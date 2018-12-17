# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
driver.switch_to_frame("iframeResult")
time.sleep(3)
driver.find_element_by_xpath("//*[@value='显示警告框']").click()
t = driver.switch_to_alert()
print(t.text)
time.sleep(3)
t.accept()