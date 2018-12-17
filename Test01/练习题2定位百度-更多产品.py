# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
mouse = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(mouse).perform()
a = driver.find_element_by_xpath(".//*[@id='head']/div/div[4]/div/div[2]/div[1]/div/div/a")
print(a.text)
time.sleep(3)
# 解决click失效办法
js = "document.getElementsByName('tj_more')[0].click()"
driver.execute_script(js)
