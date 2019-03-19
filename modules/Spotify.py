from Call import Call

class Spotify(Call):
  def __init__(self):
    self.name = "Spotify"

  def saySomething(self):
    print("Something something ", self.name)

spotify = Spotify()

print(spotify.enterCall())
print(spotify.enterNumber(5))