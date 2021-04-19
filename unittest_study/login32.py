import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def login(driver, mobile, password):
    # 打开aliyun32网址
    driver.get("http://aliyun.32.cn")
    driver.implicitly_wait(5)
    # 最大化窗口
    driver.maximize_window()
    # 点击右上角登录
    driver.find_element_by_xpath("//ul[@class='topbar-right pull-right']//a[contains(.,'登录')]").click()
    driver.implicitly_wait(5)
    # 切换登录方式
    driver.find_element_by_xpath("//i[@class='iconfont switch-icon float-right icon-shoujishumadiannao']").click()
    driver.implicitly_wait(3)
    # 切换为手机密码登录
    driver.find_element_by_xpath("//div[@class='v-tab']").click()
    time.sleep(2)
    # 输入手机号
    driver.find_elements_by_xpath("//input[@placeholder='请输入常用手机号码']")[1].send_keys(mobile)
    # 输入密码
    driver.find_element_by_css_selector("[placeholder='请输入密码']").send_keys(password)
    # 点击登录
    driver.find_element_by_css_selector(".primary.v-btn > .v-btn__content").click()
    time.sleep(10)

#判断登录是否成功
def is_login_success(driver):
    # 验证登录是否成功
    t = driver.find_element_by_xpath("//p[@class='fs16 textover']").text
    print(t)
    if t != "Hi，你好":
        return True
    else:
        return False

# 登出函数
def logout(driver):
    # 定位用户名元素位置
    move = driver.find_element_by_xpath("//*[@class='fs12 el-popover__reference']")
    # 模拟鼠标悬停
    ActionChains(driver).move_to_element(move).perform()
    # 点击退出账号
    driver.find_element_by_xpath("//*[@class='logout text-gray']").click()