# coding:utf-8
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        print("start!")
    def tearDown(self):
        print("end!")
    def test01(self):        #按照用例名称01、02、03执行
        print("执行测试用例01")
    def test03(self):
        print("执行测试用例03")
    def test02(self):
        print("执行测试用例02")
    def addtest(self):    #非test开头不会执行
        print("add方法")


if __name__ =="__main__":
    unittest.main()