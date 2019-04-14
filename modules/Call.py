import sounds

class Call:
  def __init__(self, name, options):
    self.name = name
    self.inCall = False
    self.options = options
    self.dynamicOptions = False

  def enterCall(self):
    sounds.playWeatherSounds()
    self.inCall = True

    print("You are in call with ", self.name)
    print("These are the options ", self.options)

    sounds.saySomething("Hi there. You are on call with {}. Press 1 and hold.".format(self.name))

  def enterNumber(self, number):
    print("Entered ", number, " into ", self.name)
    if not self.dynamicOptions:
      if self.options[number - 1]:
        serviceName = self.options[number]
      try:
        getattr(self, serviceName)()
      except AttributeError as error:
        print(error)
    else:
      print("Dynamic options!", number)
      # self.dynamicOption(number)

  def dynamicOption(number):
    print("dynamic options number ", number)

  def hangup(self) :
    if self.inCall:
      print("Hanging up call with ", self.name)
      sounds.stopAll()
      self.inCall = False


