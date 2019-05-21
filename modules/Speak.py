from Microphone import listen

def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = x
                return result            
    return result

class Command:
    def __init__(self, commands):
        self.commands = commands
    def reply(self):
        print("Hello to you!")

hello = Command([
    "hello",
    "hi",
    "hey",
    "greetings"
])

commands = [
  hello,
]

while True:
    userSays = listen()
    if userSays:
        print("user says {}".format(userSays))
        words = userSays.split()
        for c in commands:
            print(common_data(words, c.commands))
            if common_data(words, c.commands):
                c.reply()


