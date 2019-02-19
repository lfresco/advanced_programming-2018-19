# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:39:57 2019

@author: Lorenzo Fresco
"""

import unittest
class MyRange():
    
    def __init__(self,start,stop,step=1):
        self.range=range(start,stop,step)
        
        
def myrange(arg1, arg2 = None, step =1):
    
    if arg1 == None:
        raise TypeError('Should at least have an arg')
    addList=[]
    if arg2 != None:
        begin = arg1
        end = arg2
    else:
        begin = 0
        end = arg1
    i = begin
    while(i != end):
        addList.append(i)
        i= i + step
    return addList
        
        
    
class testmyRange(unittest.TestCase):
    
    def test_min(self):
        with self.assertRaises(TypeError):
            myRange()

    def test_equality(self):
        
        self.assertEqual(myRange(1, 11), myRange(1,11))
        self.assertEqual(myRange(21, 0, -3), myRange(21, 0, -3))


    def test_dimension(self):
        self.assertEqual(100, len(myRange(100)))

if __name__ == '__main__':
    unittest.main()
      
