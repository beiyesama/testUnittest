# coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class Aliyun32(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://aliyun.32.cn")
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u'''验证元素存在：首页'''
        locator =("xpath","//a[.='首页']")
        result = EC.text_to_be_present_in_element(locator,u"首页")(self.driver)
        self.assertTrue(result)

    def test_02(self):
        u'''验证元素存在：title：商标注册_商标查询_商标交易就在知协网'''
        result = EC.title_is(u"商标注册_商标查询_商标交易就在知协网")(self.driver)
        self.assertTrue(result)

if __name__ =="__main__":
    unittest.main()