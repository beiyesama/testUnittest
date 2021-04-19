import unittest
class Test(unittest.TestCase):
    def test01(self):
        '''判断a==b'''
        a = 1
        b = 1
        self.assertEqual(a,b)

    def test02(self):
        '''判断a in b'''
        a = "hello"
        b = "hello dbb"
        self.assertIn(a,b)

    def test03(self):
        '''判断a is True'''
        a = True
        self.assertTrue(a)

    def test04(self):
        '''失败案例'''
        a = "hello"
        b = "hi"
        self.assertEqual(a,b)

if __name__ == "__main__":
    unittest.main()

'''
assertEqual
assertNotEqual
assertIn
assertNotIn
assertTrue
assertFalse
assertIsNone
assertIsNotNone
'''