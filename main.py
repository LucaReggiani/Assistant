import speech_recognition as sr
from gtts import gTTS
import os


def take_commands():

    r = sr.Recognizer()  # The purpose of a Recognizer instance is to recognize speech.

    # This threshold is associated with the perceived loudness of the sound, but it is a
    # nonlinear relationship. The actual energy threshold you will need depends on your
    # microphone sensitivity or audio data. Typical values for a silent room are 0 to 100,
    # and typical values for speaking are between 150 and 3500. Ambient noise has a
    # significant impact on what values will work best. For this reason, it's better set
    # this property to a high value initially (4000 works well), so the threshold is
    # always above ambient noise levels.

    r.energy_threshold = 4000

    with sr.Microphone(device_index=0) as source:
        print('speak please:')

        # r.pause_threshold = 1

        # voice registration by the microphone chosen for a period of time = 5. It's possible to change it
        audio = r.record(source, duration=5)

    # saving the registration as a .wav file
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    # listening of the file and store it in the 'audio' variable
    with sr.AudioFile("microphone-results.wav") as source:
        audio = r.listen(source)

    try:
        print('Recognizing')
        # for listening the command in italian
        query = r.recognize_google(audio, language='it_IT')

    except Exception as e:

        # this method is for handling the exception and so that assistant can ask for telling again the command
        print(e)
        print("Please, repeat again")
        return "None"

    return query


def Speak(mytext):

    # Language in which you want to convert, in myu case i chosen italian
    language = 'it'
    final_text = 'You said ' + mytext

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=final_text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named command
    myobj.save("command.mp3")

    file = "command.mp3"

    # playing the audio file
    os.system("mpg123 " + file)


if __name__ == '__main__':

    while True:

        # calling function take_commands to listen the voice
        command = take_commands()

        # repetition of your command
        Speak(command)

        # it's possiblo to say which actions the assistant has to consider with a simple if statement
        if 'Python'.casefold() in command.casefold():
            # Instructions here
            pass
