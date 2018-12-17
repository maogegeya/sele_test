# coding: UTF-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
# 通过元素属性定位
 # 通过id定位百度搜索框，并输入“Python”
 # driver.find_element_by_id("kw").send_keys("python")
 # 通过name定位百度搜索框，并输入“Python”
  # driver.find_element_by_name("wd").send_keys("python")
 # 通过class定位百度搜索框，并输入“Python”
  # driver.find_element_by_class_name("s_ipt").send_keys("python")
 # 通过link(超链接)属性定位到hao123按钮，并点击
  # driver.find_element_by_link_text("hao123").click()
 # partial_link是一种模糊匹配的方式，对于超长字符串截取其中一部分
  # driver.find_element_by_partial_link_text("123").click()
# 通过xpath定位
 # 在firepath里copy出xpath地址，*为标签（如果不想指定标签名，可以用*表示任意标签；如果想制定具体某个标签，可以直接写标签名）
  # driver.find_element_by_xpath("//*[@id='kw']").send_keys("python")
 # 用xpath通过其他属性定位
  # driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("python")
 # Xpath层级，通过定位它爷爷来定位input输入框
  # driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("python")
 # xpath逻辑运算
  # driver.find_element_by_xpath("//*[@id='kw' and @autocomplete='off']").send_keys("python")
 # xpath模糊匹配功能
  # driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()
 # xpath也可以模糊匹配某个属性
  # driver.find_element_by_xpath("//*[contains(@id,'kw')]").send_keys("python")
 # xpath可以模糊匹配以什么开头
  # driver.find_element_by_xpath("//*[starts-with(text(),'hao')]").click()
 # xpath还支持最强的正则表达式（matchs和ends-with还有报错，原因不知！！！）
  # driver.find_element_by_xpath("//*[matchs(text(),'hao123')]").click()
# CSS定位（#表示id属性；.表示class属性；直接用标签名称，无任何标识符）
  # driver.find_element_by_css_selector("#kw").send_keys("python")
  # driver.find_element_by_css_selector("[name='wd']").send_keys("python")
  # driver.find_element_by_css_selector("input#kw").send_keys("python")
