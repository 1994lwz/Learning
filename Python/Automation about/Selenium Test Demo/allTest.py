#coding = utf-8  

import unittest  
import HTMLTestRunner  
import time
import sys, os
PROJECT_DIR = os.getcwd()
sys.path.append(PROJECT_DIR)
import caseList
from test_case import *

# print(os.path.dirname(os.getcwd()))
# print(os.getcwd())
# print(os.path.realpath(__file__))
# print(sys.path[0])
NOW_TIME_FORMAT = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))

REPORT_DIR = PROJECT_DIR + os.sep + "test_report" + os.sep + NOW_TIME_FORMAT
REPORT_FILENAME = REPORT_DIR + os.sep + "test_report.html"



testcases = caseList.caselist()
testsuite = unittest.TestSuite()
# testsuite.addTest(unittest.makeSuite(test_Baidu))

for testcase in testcases:
	print(testcase)
	testsuite.addTest(unittest.defaultTestLoader.loadTestsFromName(testcase))

# create report directory if not exist
if not os.path.exists(REPORT_DIR):
	os.makedirs(REPORT_DIR)

with open(REPORT_FILENAME, 'wb') as fp:

	runner = HTMLTestRunner.HTMLTestRunner(
			    stream = fp, 
			    title = 'Test Report', 
			    description = 'Test Result'
			)

	runner.run(testsuite)