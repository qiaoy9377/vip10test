import os
import unittest
from Practice.test_math import Math

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n整个unittest套件执行前一共执行一遍')
        print('----------',__name__)

    def setUp(self):
        print('执行setUp方法')

    def test_add1(self):
        print('执行add1方法')
        print('--1')
        d=math(1,2)
        expect = d.add1()
        self.assertEqual(expect,3)

    def test_add2(self):
        print('执行add2方法')
        print('--2')
        d = math(1,3)
        expect = d.add2()
        try:
            self.assertEqual(expect,3)
        except AssertionError as msg:
            print(msg)

    def tearDown(self):
        print('执行teardown')

    @classmethod
    def tearDownClass(cls):
        print('整个unittest套件执行后一共执行一遍')

if __name__ == '__main__':
    test_dir= os.path.dirname(__file__)
    print(test_dir,'11111111')
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

    #方法二：
    loader = unittest.TestLoader()
    loader.discover()
    print('----------')
    runner = unittest.TextTestRunner()
    runner.run(discover)