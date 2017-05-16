from selenium import webdriver
import sys
import time
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import  StaticLiveServerTestCase
import unittest
from selenium.webdriver.common.keys import Keys
class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):

        for arg in sys.argv:
            if "liveserver" in arg:
                cls.server_url="http://"+arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url=cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url==cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(1)
    def tearDown(self):
        self.browser.quit()

    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url)
        #self.browser.set_window_size(1024, 768)

        # 她看到输入框完美的居中显示
        inputbox = self.browser.find_element_by_id("id_new_item")
        #self.assertAlmostEqual(inputbox.location['x'] + inputbox.size["width"] / 2, 512, delta=5)

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        #伊迪丝听说有一个很酷的在线代办事项应用
        #她去看了看这个应用的首页
        self.browser.get(self.server_url)

        #她注意到网页的标题和头部都包含了To-Do这个词
        self.assertIn("To-Do",self.browser.title)
        header_text=self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do",header_text)

        #应用邀请她输入了一个待办事项
        inputbox=self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"),"Enter a to-do item")


        #它在一个文本框中输入了"购买孔雀羽毛"
        #伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys("购买孔雀羽毛")

        #她按回车键后，页面更新了
        #她被带到了一个新的URL
        #这个页面的代办事项表格中显示了 1：购买孔雀羽毛
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,"/lists/.+")
        self.check_for_row_in_list_table("1:购买孔雀羽毛")



        #页面中又显示了一个文本框，可以输入其他的代办事项
        #她输入了"使用孔雀羽毛做假蝇"
        inputbox=self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("使用孔雀羽毛做假蝇")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        #伊迪丝做事很有条理


        #页面再次更新 他的清单中显示了这两个待办事项
        self.check_for_row_in_list_table("1:购买孔雀羽毛")
        self.check_for_row_in_list_table("2:使用孔雀羽毛做假蝇")


        #现在一个叫弗朗西斯的新用户访问了网站

        ##我们启用了一个新的浏览器会话.
        ##确保伊迪丝的信息不回从cookie中泄露出来
        self.browser.quit();
        self.browser=webdriver.Firefox()

        #弗朗西斯访问首页
        #页面中看不到伊迪丝的清单
        self.browser.get(self.server_url)
        page_text=self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("购买孔雀羽毛",page_text)
        self.assertNotIn("做假蝇",page_text)

        #弗兰西斯输入了一个新的待办事项，新建一个清单
        #他不像伊迪丝那样兴趣盎然
        inputbox=self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("买牛奶")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        #弗朗西斯获取了唯一的url
        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,"/lists/.+")
        self.assertNotEqual(francis_list_url,edith_list_url)

        #这个页面还是没有伊迪丝的清单
        page_text=self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("购买孔雀羽毛",page_text)

        self.assertIn("买牛奶",page_text)

        #不错，睡觉去了







