import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """能够正确的处理像Wolfgang Amadeus Mozart"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()

# 类NameTestCase包含了一系列针对get_formatted_name()的单元测试。
# 类名可随意定义，但最好能带Test字样，来让人一眼知道是用来测试的。
# 我们运行当前文件时，所有以'test_'打头的方法都将自动运行。
# 我们使用了unittest类最有用的功能之一assertEqual()方法来测试结果的正确性
# 代码行unittest.main()让Python运行这个文件中的测试。
