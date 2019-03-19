# import sounds

class Call:
  def __init__(self, name):
    self.name = name
    self.inCall = False

  def enterCall(self):
    # sounds.playRing()
    self.inCall = True

    print("You are in call!")

    # while self.inCall:
    #   try:
    #     print("You are in the call!")
    #   except KeyboardInterrupt:
    #     break

  def enterNumber(self, number):
    self.dialedNumber = number
    print("Entered ", number, " into ", self.name)

