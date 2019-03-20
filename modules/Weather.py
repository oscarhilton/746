from Call import Call
import requests

class Weather(Call):
  def __init__(self):
    self.name = "Weather"
    self.options = {
      "1": "today",
      "2": "tomorrow",
      "3": "week"
    }
  
  def today(self):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=20d6758a5860e3fb77f974e096a6f9c5')
    print(r.json())
    