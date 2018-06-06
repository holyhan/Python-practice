import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    # 该方法将先于其他'test_'打头的方法运行。
    # 这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


# 这里在IDE环境下需要判断，否则IDE环境会先执行导入模块，再执行当前文件
if __name__ == '__main__':
    unittest.main()
