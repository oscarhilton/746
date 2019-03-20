from Call import Call
import requests
import os

class Weather(Call):
  def __init__(self):
    self.name = "Weather"
    self.options = {
      "1": "today",
      "2": "tomorrow",
      "3": "week"
    }

  def today(self):
    location = "London"
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=20d6758a5860e3fb77f974e096a6f9c5'.format(location))

    data = r.json()

    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]

    print(description, temp)
    toSay = "The weather in {} today is {} and the temp is {} degrees".format(location, description, temp)
    os.system("espeak {}".format(toSay))
