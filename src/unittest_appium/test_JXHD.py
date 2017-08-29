'''
Created on 2017年8月24日

@author: 王玉李
'''
import unittest
from appium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class JXHD_test(unittest.TestCase):
    
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
        self.driver.press_keycode(4)
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
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/add_class').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/classCheckBox').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/notice_edit').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/notice_edit').send_keys('这是一条通知短信')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/parent_checkbox').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_btn_send').click()
        send_time1 = time.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日')[0:-1]
        time.sleep(10)
        self.assertEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_type').get_attribute('name'), '通知', None)
        send_time2 = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_date').get_attribute('name')[0:-1]
        self.assertEqual(send_time1, send_time2, None)

    def test_sendMessage_homework(self):
        # 短信 - 发作业
        self.driver.find_element_by_name('短信').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/sms_homework').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/add_class').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/classCheckBox').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/choose_subjects').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/project_name').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/work_edit').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/work_edit').send_keys('这是一条作业短信')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/sing_checkbox').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_btn_preview').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        send_time1 = time.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日')[0:-1]
        time.sleep(10)
        self.assertEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_type').get_attribute('name'), '作业', None)
        send_time2 = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_date').get_attribute('name')[0:-1]
        self.assertEqual(send_time1, send_time2, None)
    
    def test_sendMessage_comment(self):
        # 短信 - 发评语
        self.driver.find_element_by_name('短信').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/sms_comments').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/add_class').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/iv_icon').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/userCheckBox').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/comment_text').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_btn_send').click()
        send_time1 = time.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日')[0:-1]
        time.sleep(10)
        self.assertEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_type').get_attribute('name'), '评语', None)
        send_time2 = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/home_sms_date').get_attribute('name')[0:-1]
        self.assertEqual(send_time1, send_time2, None)
        
    def test_classZone_notice(self):
        # 班级空间 - 公告
        self.driver.find_element_by_name('班级空间').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ll_sendnotice').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/announcement_title').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/announcement_title').send_keys('公告标题')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/announcement_edit').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/announcement_edit').send_keys('公告内容')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        send_time1 = time.strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日')[0:-1]
        time.sleep(15)
        self.driver.find_element_by_name('公告').click()
        send_time2 = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/create_time').get_attribute('name')[0:-1]
        self.assertEqual(send_time1, send_time2, None)
        # 删除公告
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/title').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_ok').click()
        time.sleep(2)
        first_time = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/create_time').get_attribute('name')[0:-1]
        self.assertNotEqual(first_time, send_time2, None)
    
    def test_classZone_dynamic(self):
        # 班级空间 - 动态
        self.driver.find_element_by_name('班级空间').click()
        time.sleep(10)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ll_senddynamic').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/edittext').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/edittext').send_keys('动态内容')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/iv_pic').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/choose_album').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/image').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/isselected').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ly_done').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        send_time1 = time.strftime('%Y-%m-%d %H:%M')[0:-1]
        time.sleep(10)
        send_time2 = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_time').get_attribute('name')[0:-4]
        self.assertEqual(send_time1, send_time2, None)
        # 点赞
        num_bef = int(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_zan_num').get_attribute('name'))
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/iv_zan').click()
        num_aft = int(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_zan_num').get_attribute('name'))
        self.assertEqual(str(num_bef + 1), str(num_aft), None)
        # 评论
        self.driver.find_element_by_name('评论').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/editText_send').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/editText_send').send_keys('评论内容')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/textView_send').click()
        time.sleep(10)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_commentcontent')

    def test_classZone_picture(self):
        # 班级空间 - 照片
        self.driver.find_element_by_name('班级空间').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ll_createalbum').click()
        album_date = time.strftime('%Y%m%d%H')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/album_name').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/album_name').send_keys(album_date)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        time.sleep(10)
        self.driver.find_element_by_name('相册').click()
        self.driver.find_element_by_name(album_date).click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        self.driver.find_element_by_name('从手机相册选择').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/image').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/isselected').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/ly_done').click()
        time.sleep(15)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/item_image').click()
        self.driver.find_element_by_name('评论').click()
        self.driver.find_element_by_name('评论').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/input_comment').clear()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/input_comment').send_keys('评论内容')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_send_comment').click()
        time.sleep(3)
        self.driver.find_element_by_name('评论内容')
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        # 长按图片删除图片
        pic_icon = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/item_image')
        press_action = TouchAction(self.driver)
        press_action.long_press(pic_icon).wait(10000).perform()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/uncheck_image').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_right').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/common_title_left').click()
        self.assertEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/album_count').get_attribute('name'), '(0)', None)
        # 删除相册
        album_icon = self.driver.find_element_by_id('com.cmcc.andedu_phone:id/album_cover')
        press_action.long_press(album_icon).wait(10000).perform()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/iv_album_del').click()
        self.driver.find_element_by_id('com.cmcc.andedu_phone:id/tv_ok').click()
        time.sleep(3)
        self.assertNotEqual(self.driver.find_element_by_id('com.cmcc.andedu_phone:id/album_name').get_attribute('name'), album_date, None)