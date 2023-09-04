import pyttsx3
import pyaudio
import webbrowser
import datetime

def sptext():

    recognizer = pyaudio.Recognizer()
    with pyaudio.Microphone() as source:
        print("I am Listening:)")
        recognizer.adjust_for_ambient_noise()
        audio = recognizer.listen(source) 

        try:
            print("Recognizing")
            audio_data = recognizer.google_recognize(audio)
            return audio_data

        except pyaudio.UnknownValueError:
            print("Unable to understand")


def textspeech():

    engine  = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0])
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 100)
    engine.say()
    engine.runAndWait()

textspeech("Hello World!")


if __name__ == "__main__":

    #if sptext().lower() == "Jarvis" :
        data1 = sptext().lower()

        
    #else:
       # print("Thanks")
