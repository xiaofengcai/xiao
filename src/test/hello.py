#coding=utf-8
from selenium import webdriver
from htmlrunner import HTMLTestRunner
import unittest,time


class See(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="https://www.baidu.com"
        self.verificationErrors = []

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

    def test_01(self):
        db=self.driver
        db.get(self.base_url)
        self.assertEqual(db.title,'ZXV10 MS90 V1.2.9.01.03')
        self.assertEqual(db.current_url,self.base_url+"/")
        time.sleep(2)
        db.close()

    def test_02(self):
        db=self.driver
        db.get(self.base_url)
        self.assertEqual(db.title,'ZXV10 MS90 V1.2.9.01.03')
        self.assertEqual(db.current_url,self.base_url+"/")
        time.sleep(2)
        db.close()


class ms90(object):
    def run(self):
        test = unittest.TestSuite()
        test.addTest(See("test_01"))
        test.addTest(See("test_02"))
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        report_file = open(r'C://Users/Administrator//Desktop//'+now+'testreport.html',"wb")
        runner = HTMLTestRunner(
            stream=report_file,
            title="自动化测试报告",
            description="自动化测试结果")
        runner.run(test)
if __name__ == "__main__":
    ms90().run()


        



