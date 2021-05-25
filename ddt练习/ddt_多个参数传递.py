import unittest
from ddt import ddt,data,unpack

list1 = [[1,2],[2,2],[2,1]]
@ddt
class Mytest(unittest.TestCase):
    @data(*list1)
    @unpack
    def test_A(self,value1,value2):
        print(value1,value2)
        self.assertEqual(value1,value2)


    @data([1,2],[2,2])
    @unpack
    def test_B(self,value1,value2):
        print(value1, value2)
        self.assertEqual(value1,value2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

