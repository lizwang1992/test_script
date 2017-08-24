'''
Created on 2017年8月17日

@author: 王玉李
'''
import unittest
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

class appOuterpay_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):  # 所用test运行前执行一次
        print('-------AppOuterpay Test-------')
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
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/btn_main_app').click()
        time.sleep(5)
        
    def tearDown(self):
        # 返回首页
        while True: 
            try:
                back_button = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left')
                back_button.click()
                time.sleep(3)
            except NoSuchElementException:
                self.driver.find_element_by_id('com.cmcc.andedu_phone:id/iv_app_close').click()
                break
    
    def test_xuexiBFB_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.25))
        
        self.driver.find_element_by_name('学习百分百').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        # self.driver.find_element_by_accessibility_id('确认支付')
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click()

    def test_xueyiXT_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.24))
        
        self.driver.find_element_by_name('学易学堂').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
    
    def test_hudongZW_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.24))
        
        self.driver.find_element_by_name('互动作文').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click()
    
    def test_xuetongSX_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.24))
        
        self.driver.find_element_by_name('学通数学').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 

    def test_yuzhitong_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.25))
        
        self.driver.find_element_by_name('语智通').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click()
    
    def test_miaobiZW_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('妙笔作文').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
    
    def test_mingshiDX_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('名师导学').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
    
    def test_kaodianJJ_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('新东方考点精讲').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_mingshiYK_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('新东方名师优课').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_Efudao_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('E辅导').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_koudaiWD_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('口袋问答').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_chengzhangBS_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('成长帮手').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_jiazhangXT_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('家长学堂').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_youjiaCZT_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('优佳成长通').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
        
    def test_mingxiaoZY_outerpay_dianbo(self):
        
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.23))
        
        self.driver.find_element_by_name('名校资源').click()
        self.driver.find_element_by_name('元/180天').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_down').click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.webkit.WebView').find_elements_by_class_name('android.view.View')[6].click()
        time.sleep(20)
        self.driver.find_element_by_class_name('android.widget.RadioButton').click() 
