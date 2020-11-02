import pyttsx3
import speech_recognition as sr


def take_commands():

    r = sr.Recognizer()  # The purpose of a Recognizer instance is to recognize speech.
    r.energy_threshold = 4000

    with sr.Microphone(device_index=0) as source:
        print('speak please:')

        # r.pause_threshold = 1
        audio = r.record(source, duration=5)
        # audio = r.listen(source)
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    with sr.AudioFile("microphone-results.wav") as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print('Recognizing')
        # for listening the command in indian english
        Query = r.recognize_google(audio, language='it_IT')
        # Query = r.recognize_sphinx(audio, language='it-IT', )
        # for printing the query or the command that we give
        print("the query is printed: '", Query, "'")


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
