# coding: UTF-8
from selenium import webdriver
# 模拟键盘操作需要先导入键盘模块
 # from selenium.webdriver.common.keys import Keys
# 鼠标事件需要先导入鼠标模块
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.baidu.com")
# ①点击鼠标左键页面按钮：Click();②清空输入框：Clear();③输入字符串：send_keys()，如果发送的是中文，则前面要加u；④submit()一般用于模拟回车键
 # driver.find_element_by_id("kw").send_keys(u"中国")
 # driver.find_element_by_id("kw").submit()
 # driver.find_element_by_id("kw").send_keys(Keys.ENTER)
# 鼠标悬停在搜索设置按钮上（move_to_element()鼠标悬停；context_click()右击鼠标；double_click()双击鼠标；perform()执行所有ActionChains中的行为）
 # mouse = driver.find_element_by_link_text("设置")
 # ActionChains(driver).move_to_element(mouse).perform()



