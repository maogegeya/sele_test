# coding: utf-8
from selenium import webdriver
import unittest
from Test01.Login_pub import Login_blog
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login_url = "https://exmail.qq.com/cgi-bin/loginpage"
        cls.driver = webdriver.Firefox()
        cls.driver.get(login_url)
        cls.driver.implicitly_wait(30)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_login(self):
        # 调用登录类里面的Login方法
        Login_blog(self.driver).login("maoge@ghcchina.com.cn","solar.163")
        time.sleep(5)
        text = self.driver.find_element_by_id("useralias").text
        print(text)
        # 断言实际结果与期望结果一致
        self.assertEqual(text,"ghcchina(maoge)")
    if __name__ == "__main__":
        unittest.main()
