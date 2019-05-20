import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

DEVICE_INDEX = 0

# Record Audio
r = sr.Recognizer()

def listen():
  with sr.Microphone(device_index=DEVICE_INDEX) as source:
    print("Say something!")
    audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

bla = listen()

print(bla)