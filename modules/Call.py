import sounds

class Call:
  def __init__(self, name, options):
    self.name = name
    self.inCall = False
    self.options = options

  def enterCall(self):
    sounds.playWeatherSounds()
    self.inCall = True

    print("You are in call with ", self.name)
    print("These are the options ", self.options)

  def enterNumber(self, number):
    print("Entered ", number, " into ", self.name)
    if number in self.options:
      serviceName = self.options.get(number)
      try:
        getattr(self, serviceName)()
      except AttributeError as error:
        print(error)


