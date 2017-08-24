'''
Created on 2017年8月10日

@author: 王玉李
'''
import unittest
from appium import webdriver
import time

class homepage_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):  # 所用test运行前执行一次
        print('----------Test Start----------')
        desired_caps = {
            'platformName':'Android',
            'deviceName':'S25QBDPD225KV',
            'platformVersion':'6.0',
            'appPackage':'com.cmcc.andedu_phone',
            'appActivity':'com.cmcc.andedu_phone.activity.guide.SplashActivity',
            'unicodeKeyboard':True,  # 使用unicode编码方式发送字符串
            'resetKeyboard':True  # 键盘隐藏
            }
        
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(10)  # 启动APP后休息10秒，等待页面加载
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('----------Test over----------')
        
    def test_search(self):
        # 点击首页搜索框，进入搜索页面
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/main_search').click()
        time.sleep(2)
        # 搜索关键字
        self.driver.find_element_by_class_name('android.widget.EditText').clear()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('化学')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ll_main_search').click()
        time.sleep(2)
        # 找到搜索结果中的咨询，点击标题
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/news_title').click()
        time.sleep(5)
        # 确定咨询页面打开，点击返回
        # self.driver.find_element_by_name('新闻资讯')
        # print(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_middle').get_attribute('name'))
        self.assertEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_middle').get_attribute('name'), '新闻资讯', None)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
