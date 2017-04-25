from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):

        #伊迪丝听说有一个很酷的在线代办事项应用
        #她去看了看这个应用的首页
        self.browser.get("http://localhost:8000")

        #她注意到网页的标题和头部都包含了To-Do这个词
        self.assertIn("To-Do",self.browser.title)
        self.fail("Finish the test!");

        #应用邀请她输入了一个待办事项

        #它在一个文本框中输入了"购买孔雀羽毛"
        #伊迪丝的爱好是使用假蝇做鱼饵钓鱼

        #她按回车键后，页面更新了

        #代办事项表格中显示了 1：购买孔雀羽毛

        #页面中又显示了一个文本框，可以输入其他的代办事项
        #她输入了"使用孔雀羽毛做假蝇"
        #伊迪丝做事很有条理

        #页面再次更新 他的清单中显示了这两个待办事项

        #伊迪丝想知道这个网站是否会记住他的清单

        #她看到网站为他生成了一个唯一的url
        #并且页面中又一些文字解说这个功能

        #她访问这个url，发现代办列表还在

        #他很满意，睡觉去啦


if __name__ =='__main__':
    unittest.main()


