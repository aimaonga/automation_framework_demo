# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from framework.base_page import BasePage


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
　　　　　这里先调用homepage类，通过homepage中的方法进行案例执行，详见代码
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法

        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    """ 这个是直接调用base_page类，元素编写格式为：id=>xx ，因为在base_page中用=>对元素进行切割，具体返回去看一下base_page中的内容
　　　　 return: 
　 　"""

    def test_baidu_search2(self):
        test = BasePage(self.driver)
        test.type("id=>kw", 'selenium')
        test.click("xpath=>//*[@id='su']")
        time.sleep(1)
        test.click("xpath=>/html/body/div[1]/div[5]/div[1]/div[3]/div[2]/div[1]/h3/a")


if __name__ == '__main__':
    unittest.main()
