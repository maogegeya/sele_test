# 导入unittest模块
import unittest
# 定义一个测试的unittest.TestCase类，并继承这个类
class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        pass # 如果没有可以不写，或者用pass代替前置条件
    def tearDown(self):
        pass # 如果没有可以不写，或者用pass代替后置条件
# test method names begin 'test*'
    def testAdd(self):
        result = 1+2
        hope = 3
        self.assertEqual(result,hope)
        self.assertEqual((1 + 2), 3)
        self.assertEqual((0 + 1), 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
if __name__ == '__main__':
# 运行主函数
    unittest.main()




