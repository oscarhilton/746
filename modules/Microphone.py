import speech_recognition as sr

DEVICE_INDEX = 0

# Record Audio
r = sr.Recognizer()
m = sr.Microphone(device_index=DEVICE_INDEX)

def printMicrophoneSources():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def say(text):
    print(text)
    return

def listen():
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        while True:
            print "Say something!"
            with m as source: audio = r.listen(source)
            print "Got it! Now to recognize it..."
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes: # this version of Python uses bytes for strings (Python 2)
                    say(u"You said {}".format(value).encode("utf-8"))
                else: # this version of Python uses unicode for strings (Python 3+)
                    say("You said {}".format(value))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                time.sleep(0.5) # sleep for a little bit
    except KeyboardInterrupt:
        pass

listen()