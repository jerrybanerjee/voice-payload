import speech_recognition as sr
import random
ExampleCommands = ["Carly open consumer by last name Banerjee" , "Hello Carly search consumer ID 1110", "Carly open consumer first name Jerry" , 
"Good morning Carly open comsumer ID 1223", "Hello Carly search consumer last name Milan","Hey Carly search consumer first name Leo "]#
def recordAudio(ExampleCommands):
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please try something like: \n",random.choice(ExampleCommands),"\n")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    data = ""
    data = r.recognize_google(audio)
    return data

def Carly(data,ExampleCommands):
    
    if "Carly" in data :
        consumerCheck(data,ExampleCommands)

    else: 
        print("Please try starting your phrase by something like Hey Carly\n")

def consumerCheck(data, ExampleCommands):
    if "consumer" in data :
        function(data)

    else :
       print("Please try saying something like: \n",random.choice(ExampleCommands),"\n")
        

def function (data):
 
    if "search" in data:
        search(data)
    elif "open" in data:
        search(data)

    

    else: 
        print("Please try something like: \n",random.choice(ExampleCommands),"\n")

def search(data):
    datas =data.split()
    length  = len(datas)
    for x in range (length):
        try:
            val = int(datas[x])
           
            payload =  {"consumerIdentifier": {"consumerAgencyIdentifier": datas[x]},"firstresult": 0,"maxresults": -1}
            print(payload)
            print("ID sucess")


        except ValueError:
            print("")


        if datas[x] == "first" :
            payload = {"consumerIdentifier":{"firstname": datas[x+2]},"firstresult": 0,"maxresults": -1}
            print("FN Sucess")
            print(payload)

        elif datas[x] == "last" :
            payload = {"consumerIdentifier": {"lastname": datas[x+2]},"firstresult": 0,"maxresults": -1}
            print("LN sucess")
            print(payload)

        elif datas[x] == "ID" :
            payload = {"consumerIdentifier": {"consumerAgencyIdentifier": datas[x+1]},"firstresult": 0,"maxresults": -1}
            print(payload)
            print("ID sucess")

        
        
            
        

    
    




   
while 1:
    data = recordAudio(ExampleCommands)
    Carly(data,ExampleCommands)

