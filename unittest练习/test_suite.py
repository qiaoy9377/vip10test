import unittest
class Testfun(unittest.TestCase):

    def setUp(self):
        self.a = 20
        self.b = 10

    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result,30)

    def teat_sub(self):
        result = self.a - self.b
        self.assertEqual(result,10)

if __name__ == '__main__':
    #创建测试用例集实例
    suite = unittest.TestSuite()
    #添加test_add方法到suite
    suite.addTest(Testfun('test_add'))
    #创建运行的实例
    runner = unittest.TextTestRunner()
    #调用运行用例集的方法
    runner.run(suite)

    #等价于手工添加全部test开头的方法
    #unittest.main()