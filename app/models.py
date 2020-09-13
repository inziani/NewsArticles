
class Articles:
  """ Articles class for defining the article objects"""
  def __init__(self, author, title, desc,img,links, publishedAt, content):
    self.author = author
    self.title = title
    self.desc = desc
    self.urlToImage = img
    self.links = links
    self.publishedAt = publishedAt
    self.content = content

class NewsSource:
  """NewSource class for creating the news sources objects"""
  def __init__(self, id, name, desc, category, language, country, url):
    self.source = id
    self.name = name
    self. desc = desc
    self.category = category
    self.language = language
    self.country = country
    self.url = url