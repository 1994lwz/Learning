#coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import unittest
import HTMLTestRunner
import time

class test_Baidu(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.baidu.com/"
		# record errors - unittests
		self.verficationErrors = []
		self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([],self.verficationErrors)

	def test_Search(self):
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").send_keys("google")
		driver.find_element_by_id("su").click()
		time.sleep(3)

	def test_BaiduSettings(self):

		driver = self.driver
		driver.get(self.base_url + "/gaoji/preferences.html")
		m=driver.find_element_by_name("NR")
		print(m)
		m.find_element_by_xpath("//option[@value='50']").click()
		time.sleep(2)

		driver.find_element_by_xpath("//input[@value='保存设置']").click()
		time.sleep(2)
		alert = driver.switch_to_alert()
		print(alert.text)
		alert.accept() 

if __name__ == '__main__':
	unittest.main()