from flask import render_template
from app import app
from ..requests import get_top_headlines
import os


@app.route('/')   
def index():
  """ This view imports the top headlines"""
  title = 'newsbites'
  topheadlines = get_top_headlines()
  return render_template('index.html', context = topheadlines, title=title)




