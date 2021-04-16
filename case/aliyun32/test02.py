# coding:utf-8
import unittest

'''
setup():每个测试case运行前运行
teardown():每个测试case运行完后执行
setUpClass():必须使用@classmethod 装饰器,所有case运行前只运行一次
tearDownClass():必须使用@classmethod装饰器,所有case运行完后只运行一次
'''
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")
    @classmethod
    def tearDownClass(cls):
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