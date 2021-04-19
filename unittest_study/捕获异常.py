# coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

driver = webdriver.Chrome()
driver.get("http://aliyun.32.cn")
try:
    element = driver.find_element_by_xpath("//a[.='商标注册xxx']")
except NoSuchElementException as msg:
    print(u'查找元素异常%s' % msg)
    driver.quit()
except ElementNotVisibleException as msg:
    print(u'元素不可见%s'%msg)
else:
    element.click()
    driver.implicitly_wait(10)
    driver.quit()
'''
selenium常见异常

1.NoSuchElementException：没有找到元素

2.NoSuchFrameException：没有找到iframe

3.NoSuchWindowException:没找到窗口句柄handle

4.NoSuchAttributeException:属性错误

5.NoAlertPresentException：没找到alert弹出框

6.ElementNotVisibleException：元素不可见

7.ElementNotSelectableException：元素没有被选中

8.TimeoutException：查找元素超时
'''