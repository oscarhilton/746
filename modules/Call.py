# import sounds

class Call:
  def __init__(self, name):
    self.name = name
    self.inCall = False

  def enterCall(self):
    # sounds.playRing()
    self.inCall = True

    print("You are in call with ", self.name)

  def enterNumber(self, number):
    print("Entered ", number, " into ", self.name)

