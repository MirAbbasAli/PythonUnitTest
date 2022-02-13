'''
Created on Feb 13, 2022

@author: abbas
'''
## Making necessary imports
import unittest
from test.circle import Circle
from math import pi

object1=None
#setUpModule-instantiates the objects and returns the same
def setUpModule():
    object1=Circle()
    print("Module")
    return object1

#tearDownModule-uninstantiates the objects
def tearDownModule():
    print("tear down module")
    object1=None
    

class Test1(unittest.TestCase):
    radius=-2
    #setUpClass creates a list of test data
    @classmethod
    def setUpClass(cls):
        cls.a=[-2,3-2j,True, 10]
        
    @classmethod
    def tearDownClass(cls):
        print("In tear down class method")
        
    def setUp(self):
        print("before test method")
        
    def tearDown(self):
        print("after test method")
    
    def test_3(self):
        # test when radius > 0
        cObject=setUpModule()
        self.assertAlmostEqual(cObject.circle_area(self.a[3]),pi*100)
    
    @unittest.skipIf(radius<0,"negative_value")
    @unittest.expectedFailure
    def test_4(self):
        setUpModule().circle_area(self.a[0])
    
    @unittest.skipUnless(type(radius) in [int, float], "Non-numeric value")
    @unittest.expectedFailure
    def test_5(self):
        setUpModule().circle_area(self.a[1])
    
    @unittest.expectedFailure    
    def test_2(self):
        cObject=setUpModule()
        self.assertRaises(TypeError,cObject.circle_area(self.a[1]))
        
    @unittest.expectedFailure    
    def test_1(self):
        print("test1")
        print(setUpModule().circle_area(self.a[0]))       