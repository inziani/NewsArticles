from app import app 
from newsapi import NewsApiClient
import os
from .models import Articles

#Article = article.Articles

def get_top_headlines():



  """Function that formats the data from API into a list using the zip 
      function ready for consumption"""
      
  newsapi = NewsApiClient(api_key=os.environ.get("API_KEY"))
  topheadlines = newsapi.get_top_headlines(sources = "CNN, bbc-news, techcrunch.com, al-jazeera-english")
  articles = topheadlines['articles']

  author = list()
  title = list()
  desc = list()
  img = list()
  links = list()
  publishedAt = list()


  for i in range(len(articles)):
    myarticles = articles[i]
    author.append(myarticles['author'])
    publishedAt.append(myarticles['publishedAt'])
    title.append(myarticles['title'])
    desc.append(myarticles['description'])
    img.append(myarticles['urlToImage'])
    links.append(myarticles['url'])

  myList = zip(author, publishedAt, title, desc, img, links)
  return myList

    
