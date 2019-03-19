from Call import Call

class Spotify(Call):
  def __init__(self):
    self.name = "Spotify"
    self.options = {
      "1": "trackDetails",
      "2": "2",
      "3": "3"
    }