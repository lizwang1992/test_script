'''
Created on 2017年8月24日

@author: 王玉李
'''
import unittest
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

class homepage_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):  # 所用test运行前执行一次
        print('----------JXHD Test----------')
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
        
    def setUp(self):
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/rb_home').click()
        time.sleep(5)
        
    def tearDown(self):
        # 返回首页
        while True: 
            try:
                back_button = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left')
                back_button.click()
                time.sleep(1)
            except NoSuchElementException:
                break
    
    def test_sendMessage_notice(self):
        # 短信 - 发通知
        self.driver.find_element_by_name('短信').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/sms_notice').click()
        time.sleep(5)
