# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import sys


# Initialize
r = sr.Recognizer()

audioTextFile = open('audioTextFile.txt', 'w')


# convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while(1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # ~ second lag
            r.adjust_for_ambient_noise(source2, duration=0.2)

            #listens user's input
            audio2 = r.listen(source2)

            # google recognize audio
            audio = r.recognize_google(audio2)
            audio = audio.lower()

            print(audio)
            SpeakText(audio)
            audioTextFile.write(audio + " ")



    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
