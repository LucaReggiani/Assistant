# Assistant

this project has the aim to create a simple and useful assistant for the operative system. This is tested on Linux

## Packages explanation:

 - **SpeechRecognition:** <p> Library for performing speech recognition, with support for several engines 
                      and APIs, online and offline.</p>
                      <p>More info [here](https://pypi.org/project/SpeechRecognition/). In order to 
                      install the library:</p>
 
       pip install SpeechRecognition
 
 - **gTTS:** <p> A Python library and CLI tool to interface with Google 
         Translate’s text-to-speech API. Writes spoken mp3 data to a file, a file-like object 
         (bytestring) for further audio manipulation, or stdout. It features flexible 
         pre-processing and tokenizing, as well as automatic retrieval of supported languages.</p>
         <p>More info [here](https://gtts.readthedocs.io/en/latest/). In order to install the library:</p>
            
       pip install gTTS
       
 Please, check the docs of these packages in order to check if other dependencies are required.
 
## explaination of the project

when the program starts, it's requested to the user to speek. During this time, each word that the user say for 5 seconds is recorded.
After 5 seconds, the registration is saved into the 'microphone-results.wav' file. Then, the file is reopened and its content 
is listened by the Recognizer object. if the command is recognized, it is converted in a string and stored in a variable in the main.
if the command is not recognized, the program asks at the user to repeat again. 
When the command will be recognized, the program pass the string to the gTTS method, that will convert the text in 
audio format and will save it in another file. Finally, this file is reproduced by mpg123 software, that is 
explained [here](https://www.mpg123.de/).          
 
