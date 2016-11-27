#coding:utf8
'''
Created on 2016年5月7日

@author: zhongqiang
'''
import unittest
from my_doctest import hello_add,hello_substract
from train.day03.Class_demo import User

class Test(unittest.TestCase):
    
    def setUp(self): #声明一个类
        self.user = User()
    
    def test_hello_add(self):
        z = hello_add(x=5, y=10)
        
        assert 15 == z
        
        z1 = hello_add(12, 1)
        assert z1 == 13
    
    def test_calc(self):
        
        z = hello_substract(hello_add(3, 2),5)
        assert z == 0
        
#     def test_get_register_days(self):   #测试类方法
#         user2 = User()
#         assert user2.id == 0 
#         assert 720 == self.user.get_register_days()

    def test_user_username(self):
        assert "ttxs" == self.user.username

    def tearDown(self): #测试完成后，销毁
        unittest.TestCase.tearDown(self)


if __name__ == "__main__":
    unittest.main()


