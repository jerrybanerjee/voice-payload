# voice-payload
## Introduction
Artificial Intelligence or AI is talking over the now a days. Artificial intelligence is when the computer is trained to perform certain tasks like humans.  It is used everywhere in offices to factories to schools to homes. It just seems to be every where. **This is a AI/ voice assistant called Carly**. Carly is responsable for creating a Payload that is made through voice commands. These Payloads are then feed into the Server. 

The servers already has REST web services. The sever then decrypts the payload and then searches or open the consumer and then sends a response to the user.

## Depencies
This program is built with python 3.6.7. It is very important to install the right version of python as if you install the python version 3.7 + it would not work as this would as Pyaudio is not supported with the latest version of python. If you are installing python 3.6.7 please remember to click the option **to add to PATH.** 


![alt text](https://www.quickdevnotes.com/wp-content/uploads/2018/09/install.png  "Python Installer")

**PLEASE DO NOTE THAT I HAVE USED PYTHON3.6.6 AS AN EXAMPLE BUT PYTHON 3.6.7 HAS THE THE SAME OPTION AT THE SAME PLACE**

Onece python 3.6.7 has been installed go to your command prompt and install Pyaudio by the following commands : 
1. pip  install PyAudio
2. pip install SpeechRecognition
3. pip install requests
4. The Json and the random module is pre built in python thus you would not need to to install it through pip.

Make sure that these modules are installed as the program will not fucntion without these modules as they are not pre installed with python.

If you have more than one version of python installed in your device please make sure you remove the other python from the path as that might cause some issues in the future. 
 

## Voice Extraction 
Voice Extraction, this is one of the most important parts of the program. The program first detects the voice and then converts it into a string. This is done through the Speech Recognition module. If you want to read more about this module click [here](https://pypi.org/project/SpeechRecognition/)

Please note that the module will only work in the following versions of python 2.6, 2.7, or 3.3 - 3.6.7. Once the input is coverted into one big string. The input is split into diffrent words. This is then feed into another function that would then look for key words which would result in then the program making decitions according to the key word detected.

If the program does not understand what the input is it would display a message saying "Sorry I could not understand what you were saying " and then would prompt you to say another phrase. The program would then try to do the same process all over again.
## Payload Generation 
Generating the payload would also be very important part of the process. This payload would be feed into the server/REST services which would then result in the program beign able to retive data. It is very important that the payload is constucted properly as if it is not it would result in the wrong data getting retrived. 

When the program recives data from the user it trys to detct certain words and looks for them in the data provided. For example if the data has a number in it, the program would detect that and would construct a payload for ID. If the data have a word "first" in it, the program would detct that and would construct a payload for first name. If the the data has the word "last" in it it would detct that and would construct a payload for last name.

Once this is done it feeds the payload onto the server and gets the data back and displays it to the user. This process is then repeated again with new data.




## Tests 
Testing is one of the most important parts of programming. This helps the programer in various number of ways. If testing is performed perfectly it would help the programmer to discover flaws with the program and would also help them to efficiently improve the code.

There are sevral diffrent ways of testing :

1. Test plans 
2. Unit test
3. System testing
4. And Many more!!

I have attachted some testing methods of this program. **PLEASE DO READ THE COMMENTS IN THE UNIT TEST PROGRAMS**