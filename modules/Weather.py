from Call import Call
from weather import Weather, Unit

class Weather(Call):
  def __init__(self):
    self.name = "Weather"
    self.options = {
      "1": "today",
      "2": "tomorrow",
      "3": "week"
    }
  
  def today(self):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location("London")
    condition = location.condition
    print(condition.text)
    