# codign: utf-8
from selenium import webdriver
from selenium.common.exceptions import *    # 导入所有异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# 封装定位方法
def find_element(locator, timeout = 10):
    '''定位方法封装成函数'''
    element = WebDriverWait(driver,timeout,1).until(lambda x: x.find_element(*locator))
    return element
# 输入搜索内容
input_loc = ("id","kw")
find_element(input_loc).send_keys(u"中国")
# 点击搜索按钮
button_loc = ("id","su")
find_element(button_loc).click()
# Lambda函数，是一个匿名函数，创建语法：
#  lambda parameters:express
# parameters：可选，如果提供，通常是逗号分隔的变量表达式形式，即位置参数。
# expression：不能包含分支或循环（但允许条件表达式），也不能包含return（或yield）函数。如果为元组，则应用圆括号将其包含起来。