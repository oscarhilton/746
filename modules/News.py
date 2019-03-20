from Call import Call
import requests
import sounds
import os

class News(Call):
  def __init__(self):
    self.name = "News"
    self.options = {
      "1": "headlines",
    }

  def enterCall(self):
    sounds.playNewsSounds()
    self.inCall = True

    print("You are in call with ", self.name)
    print("These are the options ", self.options)

  def headlines(self):
    sources = "bbc-news"
    r = requests.get('https://newsapi.org/v2/top-headlines?sources={}&apiKey=cfb2ed55add84931be4a7e8ae66cf053'.format(sources))

    data = r.json()

    articles = data["articles"]

    os.system('flite -t "I find your lack of faith disturbing." ')

    for article in articles:
      print(article["title"])