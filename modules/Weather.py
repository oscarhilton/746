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
    self.weather = Weather(unit=Unit.CELSIUS)
    self.location = self.weather.lookup_by_location("London")
  
  def today(self):
    condition = self.location.condition
    print(condition.text)
    