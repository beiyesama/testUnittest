# coding:utf-8


'''
testData = [{'mobile': '15658678027', 'password': '123456dbb'},
            {'mobile': '19965412404', 'password': '654321dbb'}]
@ddt.ddt
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")
    @classmethod
    def tearDownClass(cls):
        print("end!")
    @ddt.data(*testData)
    def test(self,data):
        print(data)

if __name__ == "__main__":
    unittest.main()

'''
import ddt #测试类前加@ddt.ddt 测试case前加@ddt.data(参数)或@data(*参数)
import unittest
from selenium import webdriver
from xlrd读取excel import ExcelUtil
from login32 import login,is_login_success
import os
import HTMLTestRunner

#测试数据
path = r"A:\testUnittest\unittest_study\test.xlsx"
name = "Sheet1"
data = ExcelUtil(path,name)
testData = data.dict_excel()

@ddt.ddt
class Login32(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()

    @ddt.data(*testData)
    def test_login(self,data):
        u'''登录案例'''
        print("当前测试数据：%s" % data)
        #调用登录函数
        login(self.driver,data["mobile"],data["password"])
        #判断结果
        result = is_login_success(self.driver)
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()
