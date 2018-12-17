# coding:utf-8
# 第一步导入webdriver模块
from selenium import webdriver
# 第二步打开浏览器
# 导入time模块
import time
# 加载Firefox配置
# profile_directory = r"C:\Users\Solar Mao\AppData\Roaming\Mozilla\Firefox\Profiles\bt7z2bn9.default"
# profile = webdriver.FirefoxProfile(profile_directory)
# driver=webdriver.Firefox(profile)
driver = webdriver.Firefox()
 # driver = webdriver.Ie() IE浏览器用这个
 # driver = webdriver.Chrome() 谷歌浏览器用这个
# 第三步打开百度
driver.get("https://www.baidu.com")
# 设置休眠时间3秒，也可以是小数，单位是秒
time.sleep(3)
driver.get("http://www.hordehome.com")
time.sleep(5)
# 返回上一页
driver.back()
time.sleep(3)
# 切换到下一页
driver.forward()
time.sleep(3)
# 页面刷新
driver.refresh()
# 设置窗口大小为指定尺寸
driver.set_window_size(540,960)
time.sleep(3)
# 设置窗口最大化
driver.maximize_window()
time.sleep(3)
# 截屏
driver.get_screenshot_as_file("E:\学习资料\S+P\Test\B1.jpg")
# driver.quit()用于退出浏览器进程；driver.close()关闭当前窗口
driver.quit()


