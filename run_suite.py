import time
import unittest

from HTMLTestRunner import HTMLTestRunner

from case.TestTPShopUser import TestUser

suite = unittest.TestSuite()
# suite.addTest(TestUser("test_login"))
suite.addTest(unittest.makeSuite(TestUser))
# suite.addTest(TestUser("test_loging"))
file_to = "./report/report.html"
with open(file_to, "wb") as f:
    runner = HTMLTestRunner(f, title="我的报告", description="vio.1")
    runner.run(suite)
