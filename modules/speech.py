from gtts import gTTS
import os

# Creates an audiofile from the textfile that is created by an llm. 
def create_audio():
    gpt = ""
    with open("gpt.txt", "r") as text:
        gpt = text.read()

    audio= gTTS(gpt, lang='de')

    audio.save("weatherforecast.mp3")


    os.system("afplay weatherforecast.mp3")
    os.remove("weatherforecast.mp3")
    os.remove("gpt.txt")

if __name__ == "__main__":
    create_audio()
    
