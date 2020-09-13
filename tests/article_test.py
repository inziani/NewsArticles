import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.Testcase):

"""Test case to check the articles creation"""

  def setUp(self):
    """Set up method that will run before every test"""
    self.new_article = Article(self, news, desc, img, links)

  def test_instance(self):
  self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()