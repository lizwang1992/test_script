'''
Created on 2017年8月10日

@author: 王玉李
'''
import unittest
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

class homepage_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):  # 所用test运行前执行一次
        print('--------Homepage Test--------')
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
        print('--------Test Over--------')
     
    def tearDown(self):
        # 返回首页
        self.driver.press_keycode(4)
        while True: 
            try:
                back_button = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left')
                back_button.click()
                time.sleep(1)
            except NoSuchElementException:
                break
               
    def test_search(self):
        # 首页搜索功能
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

    def test_tagEdit(self):
        # 首页标签编辑
        # 滑动至找到“更多”编辑标签
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        while True:
            try:
                edit_button = self.driver.find_element_by_name('更多')
                edit_button.click()
                break
            except NoSuchElementException:
                self.driver.swipe(int(x * 0.8), int(y * 0.36), int(x * 0.3), int(y * 0.36))
        time.sleep(3)
        # android端需点击标签才能显示删除按钮
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tag_bg').click()
        # 找到删除第一个能删除的标签，删除并记录
        selected_tags = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/recycler_view')
        tags = selected_tags.find_elements_by_id('com.cmcc.andedu_phone:id/tag_bg')
        '''for t in tags:
            try:
                t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_delete')
                first_tag = t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_title').get_attribute('name')
                t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_delete').click()
                break
            except NoSuchElementException:
                first_tag = ''
        print(first_tag)'''
        t = tags[0]
        first_tag = t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_title').get_attribute('name')
        if '作业' == first_tag:
            t = tags[1]
            first_tag = t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_title').get_attribute('name')
        # print(first_tag)
        t.find_element_by_id('com.cmcc.andedu_phone:id/tagview_delete').click()
        # 找到刚删除的标签,添加回去
        if '' != first_tag:
            try:
                edit_button = self.driver.find_element_by_name(first_tag)
                edit_button.click()
            except NoSuchElementException:
                self.driver.swipe(int(x * 0.5), int(y * 0.8), int(x * 0.5), int(y * 0.25))
                edit_button = self.driver.find_element_by_name(first_tag)
                edit_button.click()
                self.driver.swipe(int(x * 0.5), int(y * 0.25), int(x * 0.5), int(y * 0.8))
        # 保存设置，查看标签是否添加
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        time.sleep(5)
        self.driver.find_element_by_name(first_tag)
    
    def test_myappEdit(self):
        # 我的应用编辑
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/myapp_layout').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        del_app = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/item_text').get_attribute('name')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/check_image').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_ok').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        # 多按一次返回才能返回首页
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        # 查看是否删除成功
        first_app = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/app_title').get_attribute('name')
        self.assertNotEqual(del_app, first_app, None)
