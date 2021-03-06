from Call import Call
import requests
import sounds

class Weather(Call):
  def __init__(self):
    self.name = "Weather"
    self.options = ["today", "todayRain"]
    self.appId = "20d6758a5860e3fb77f974e096a6f9c5"
    self.location = "London"
    print(self.options)

  def today(self):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(self.location, self.appId))

    data = r.json()

    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]

    toSay = "The weather in {} today is {} and the temperature is {} degrees.".format(self.location, description, temp)

    sounds.saySomething(toSay)
    sounds.saySomething("I hope you have a great day.")

  def rainToday(self):
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID={}'.format(self.location, self.appId))

    data = r.json()
    forecast = data["list"]

    hasRain = any(item.weather.main == "Rain" for item in forecast)

    if hasRain:
      toSay = "Looks like there could be rain today, be prepared!"
    else:
      toSay = "No rain forecasted today."

    sounds.saySomething(toSay)

  def dynamicOptions(number):
    print(number)
