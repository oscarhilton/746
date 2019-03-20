from Call import Call
import requests
import json
from espeak import espeak

class Weather(Call):
  def __init__(self):
    self.name = "Weather"
    self.options = {
      "1": "today",
      "2": "tomorrow",
      "3": "week"
    }

  def enterCall(self):
    espeak.synth("Welcome to the weather! To check todays weather press 1.")
  
  def today(self):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=20d6758a5860e3fb77f974e096a6f9c5')
    data = json.loads(r.json())

    print(data)

    description = data.weather.description
    temp = data.main.temp

    print(description, temp)

    # toSpeak = "Todays weather is {} and will have an average temperature of {}".format(description, temp)

    # espeak.synth(toSpeak)
    