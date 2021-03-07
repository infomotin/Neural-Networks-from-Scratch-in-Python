import pyttsx3
import datetime
import speech_recognition as sound

# biuld enggin to
enggin = pyttsx3.init()


def spack(audio):
    enggin.say(audio)
    enggin.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    spack(time)


spack('Hello World')
time()


def get_commend():
    r = sound.Recognizer()
    with sound.Microphone() as sourch:
        print("Plse continus ")
        r.pause_threshold = 1
        audio = r.listen(sourch)

    try:
        print('ok')
        qu = r.recognize_google(audio, language='en-in')
        spack(qu)
        print('Quite')
    except Exception as e:
        print(e)
        return None
    return qu


get_commend()
