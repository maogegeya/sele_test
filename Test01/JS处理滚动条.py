# coding: utf-8
from selenium import webdriver
import time
url = "https://www.hao123.com"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
time.sleep(3)
# 滚动条拉到底部
# js = "var q=document.documentElement.scrollTop=10000"  # Chrome是js = "var q=document.body.scrollTop=10000"
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js) # scrollto函数不存在浏览器兼容性问题
time.sleep(3)
# 滚动条回到顶部
# js = "var q=document.documentElement.scrollTop=0" # Chrome是js = "var q=document.body.scrollTop=0"
js = "window.scrollTo(0,0)"
driver.execute_script(js)
# 聚焦元素
target = driver.find_element_by_xpath(".//*[@id='coolsite-tuijian-group-cate']/span[1]/a")
driver.execute_script("arguments[0].scrollIntoView();",target)
print(target.text)
# driver.find_element_by_link_text("京东商城").click() 未调试成功！！！
time.sleep(3)
driver.quit()

