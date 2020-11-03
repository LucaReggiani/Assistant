import speech_recognition as sr
from gtts import gTTS
import os


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
        # print("the query is printed: '", Query, "'")

    except Exception as e:

        # this method is for handling the exception and so that assistant can ask for telling again the command
        print(e)
        print("Please, repeat again")
        return "None"

    return Query


def Speak(mytext, understand=False):

    # Language in which you want to convert
    language = 'it'

    if understand == True:
        final_phrase = 'Hai detto ' + mytext + '?'
    else:
        final_phrase = mytext
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    try:
        myobj = gTTS(text=final_phrase, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome
        myobj.save("welcome.mp3")
    except Exception as ex:
        return ex

    else:
        file = "welcome.mp3"
        os.system("mpg123 " + file)

if __name__ == '__main__':

    # Speak('Ricevuto! apro il dizionario')
    while True:

        command = take_commands()
        print(command)
        if 'calendario'.casefold() in command.casefold():
            try:
                Speak(command, understand=True)
            except Exception as ex:
                Speak('Spiacente, per un mal funzionameto è necessario ripetere!')
                continue

        elif 'Spotify'.casefold() in command.casefold():
            try:
                Speak(command, understand=True)

            except Exception as ex:
                Speak('Spiacente, per un mal funzionameto è necessario ripetere!')
                continue

        elif 'facebook'.casefold() in command.casefold():
            try:
                Speak(command, understand=True)

            except Exception as ex:
                Speak('Spiacente, per un mal funzionameto è necessario ripetere!')
                continue

        elif 'google'.casefold() in command.casefold():
            try:
                Speak(command, understand=True)

            except Exception as ex:
                Speak('Spiacente, per un mal funzionameto è necessario ripetere!')
                continue

        else:
            try:
                Speak('Non ho capito! Ripeti per favore')
            except Exception as ex:
                Speak('Spiacente, per un mal funzionameto è necessario ripetere!')
                continue
