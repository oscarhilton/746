from Call import Call
from weather import Weather, Unit

class Weather(Call):
  def __init__(self, location, unit=Unit.CELSIUS):
    self.name = "Weather"
    self.options = {
      "1": "today",
      "2": "tomorrow",
      "3": "week"
    }
    self.weather = Weather(unit=unit)
    self.location = self.weather.lookup_by_location(location)
  
  def today(self):
    condition = self.location.condition
    print(condition.text)
    