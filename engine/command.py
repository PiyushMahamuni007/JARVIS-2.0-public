import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('rate', 174)
        eel.DisplayMessage(text)
        engine.say(text)
        eel.receiverText(text)
        engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        eel.DisplayMessage(query)
        time.sleep(1)
          # Speak ut the recognized text
        

    except Exception as e:
        
        return "Say that again please..."
    return query

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takeCommand().lower()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
        
    try:
        

        if 'open' in query:
         from engine.features import openApp
         openApp(query)

        elif'on youtube' in query:
         from engine.features import playYoutube
         playYoutube(query)

        elif "send message" in query or "call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takeCommand()
                    
                elif "whatsapp call" in query:
                    flag = 'whatsapp call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name) 
         

        else:
         print("Please say the command again.")
    except:
        print("error")
    eel.DisplayHood()


