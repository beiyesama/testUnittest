# coding:utf-8
import unittest
import os
import HTMLTestRunner
#用例路径
case_path = os.path.join(os.path.dirname(os.path.relpath(__file__)),"case") #获取当前目录下的case目录
#报告存放路径
report_path = os.path.join(os.path.dirname(os.path.relpath(__file__)),"report")

# discover方法里面有三个参数：
#
# -case_dir:这个是待执行用例的目录。
#
# -pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
#
# -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover
if __name__ == "__main__":
    #runner = unittest.TextTestRunner()

    report_path = r"A:\testUnittest\report\report.html"
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'这是我的自动化测试报告',description=u'用例执行情况')
    runner.run(all_case())
    fp.close()