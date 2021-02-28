import pyttsx3

# biuld enggin to
enggin = pyttsx3.init()


def spack(audio):
    enggin.say(audio)
    enggin.runAndWait()


spack('Hello World')
