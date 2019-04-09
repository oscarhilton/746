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

    sounds.saySomething("Hi there. You are on call with {}. Press 1 and hold.".format(self.name))

  def enterNumber(self, number):
    print("Entered ", number, " into ", self.name)
    if number in self.options:
      serviceName = self.options.get(number)
      try:
        getattr(self, serviceName)()
      except AttributeError as error:
        print(error)
        
  def hangup(self) :
    print("Hanging up call with ", self.name)
    self.inCall = False
    sounds.stopAll()


