# coding: utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://baidu.csmayo88.com/kqys/?bd2pc-YY-csyyl-09200707")
time.sleep(5)
js = 'document.getElementById("swtbox").style.display="none";'
driver.execute_script(js)
time.sleep(3)