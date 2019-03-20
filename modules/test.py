from gtts import gTTS
from io import BytesIO

my_var = "hello"
mp3_fp = BytesIO()
tts = gTTS(my_var, "en")
tts.write_to_fp(mp3_fp) 
