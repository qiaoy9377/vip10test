import unittest
from ddt import ddt,data,unpack,file_data

data_list = [{'id':1,'name':'Tom','age':20},{'id':2,'name':'Rose','age':21},{'id':3,'name':'Lily','age':19}]
@ddt
class MyTestCase(unittest.TestCase):

    @file_data('D:\Python Automated Testing\ddt练习\data.json')
    def test_readjson(self,value):
        print(value)
        self.assertEqual(value,0)

    @data(*data_list)
    @unpack
    def test_readlist(self,id,name,age):
        print(id,name,age)
        self.assertNotEqual(age,20)




if __name__ == '__main__':
    unittest.main(verbosity=2)
