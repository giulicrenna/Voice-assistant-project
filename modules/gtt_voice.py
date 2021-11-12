import os
from gtts import gTTS

try:
    def say(text):
        speech = gTTS(text = text, lang = 'es', slow = False)
        speech.save("text.mp3")
        os.system("mp3-decoder -q text.mp3")
        os.system("rm text.mp3")
except KeyboardInterrupt:
    pass