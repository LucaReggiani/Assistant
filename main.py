import pyttsx3
import speech_recognition as sr


def take_commands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.7
        audio = r.listen(source)
        print("Ciao")
        try:
            print('Recognizing')
            # for listening the command in indian english
            Query = r.recognize_google(audio, language='en-in')
            # for printing the query or the command that we give
            print("the query is printed='", Query, "'")

        except Exception as e:

            # this method is for handling the exception and so that assistant can ask for telling again the command
            print(e)
            print("Please, repeat again")
            return "None"
        return Query


def Speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':

    while True:

        command = take_commands()
