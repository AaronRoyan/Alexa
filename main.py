from re import search
from tracemalloc import take_snapshot
import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime
import wikipedia as wiki
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hi, i am Alexa")
engine.say("How may i help you")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def receiveCommand():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
            else:
                print('Start Sentence with Alexa')
    except:
        talk('Network Error Occured') 
        print('Network Error Occured') 
    return command

def run():
    command = receiveCommand()
    print(command)
    if 'play'in command:
        song = command.replace('play','')
        talk('playing'+song)
        print('playing '+song+'...')
        pwk.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('the time is'+time)
    elif 'wikipedia' or 'what is' or 'who is' or 'search' or 'tell me about' in command:
        search = command.replace('wikipedia','').replace('what is','').replace('who is','').replace('search','').replace('tell me about','')
        info = wiki.summary(search, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'whatsapp' or 'whats app' or 'send message' in command:
        talk("what would you like to say?")
        response = command.replace('whatsapp','').replace('whats app','').replace('send message','')
        number = talk('whats is the number?')
        pywhatkit.sendwhatmsg(number,response)
        print("Successfully Sent!")

    else: 
        talk("im sorry, i didnt get that. Could you repeat it once again")

while True:     
    run()