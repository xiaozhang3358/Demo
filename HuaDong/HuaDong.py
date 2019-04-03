import time
from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = '8928dfbc'
# 指定appium框架版本 获取toast消息必须 指定以下参数
# desired_caps['automationName'] = 'Uiautomator2'
# 设置中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app的信息
desired_caps['appPackage'] = 'com.example.w.kuaihuishou'
desired_caps['appActivity'] = '.view.activity.StartPageActivity'

# desired_caps['appActivity'] = '.view.activity.loginmodel.LoginActivity'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 向上滑动
def swipe_up(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.75  # 起点y坐标
    y2 = s['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动
def swipe_down(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.25  # 起点y坐标
    y2 = s['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向左滑动
def swipe_left(driver, t=500, n=1):
    s = driver.get_window_size()
    x1 = s['width'] * 0.75
    y1 = s['height'] * 0.5
    x2 = s['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 向右
def swipe_right(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


if __name__ == '__main__':
    print(driver.get_window_size())  # 打印一下尺寸
    time.sleep(3)
    # 向左滑动一次
    swipe_left(driver)
    time.sleep(1)
    # 向左滑动一次
    swipe_left(driver)
    time.sleep(1)
    # 向左滑动一次
    swipe_left(driver)
    time.sleep(5)