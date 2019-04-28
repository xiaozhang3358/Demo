import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class GetPicture():
    # 类的初始化
    def __init__(self):
        # 给请求指定一个请求头来模拟chrome浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        # 要访问的网址
        self.web_url = 'https://unsplash.com'
        # 设置图片要存放的文件
        self.folder_path = 'E:\picture'

    # 封装requests请求：
    def requests(self, url):
        # 向目标url地址发送get请求，返回一个response对象
        r = requests.get(url, headers=self.headers)
        return r

    # 创建文件的方法
    def mkdir(self, path):
        # 去掉路径前后的空格或者换行符
        path = path.strip()
        # 判断文件夹是否存在
        isexists = os.path.exists(path)
        if not isexists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已存在！！')

    # 创建保存图片的方法
    def save_img(self, url, name):
        print('开始请求图片地址，请耐心等候。。。')
        img = self.requests(url)
        # time.sleep(5)
        file_name = name + '.jpg'
        print('开始保存图片。。。')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    # 逻辑部分，爬取图片的url
    def get_pic(self):
        print('开始网页get请求。。。')
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.web_url)
        # r = self.requests(self.web_url)
        # self.scorll_down(driver=driver, times=3)
        print('开始获取所有的img标签')
        all_img = BeautifulSoup(driver.page_source, 'lxml').find_all('img', class_='_2zEKz')
        # all_img = BeautifulSoup(r.text, 'lxml').find_all('img', class_='_2zEKz')
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        # 获取img标签的数量
        # print('img标签的数量是：',len(all_img))
        # 获取图片的url
        for img in all_img:
            img_url = img.get('src')
            if img_url != None:
                name_start = img_url.index('photo')
                name_end = img_url.index('?')
                img_name = img_url[name_start: name_end]
                print(len(img_name))
                self.save_img(img_url, img_name)
        # driver.close()

    # 封装下拉加载的方法
    def scorll_down(self, driver, times):
        for i in range(times):
            print('开始执行第' + str(i + 1) + '次下拉操作')
            # 下拉至最底部
            js = "window.scrollTo(0, document.body.scrollHeight)"
            driver.execute_script(js)
            print('第' + str(i + 1) + '次下拉操作执行完毕！')
            print('第' + str(i + 1) + '次等待网页加载。。。')
            time.sleep(10)


# 创建一个类的实例
pic = GetPicture()
# 执行类中的方法
pic.get_pic()
