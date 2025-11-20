import subprocess
import webbrowser
import re
import sqlite3 
import playsound as playsound
import eel
import pyautogui
from engine.command import speak
from engine.config import Assistant_name
import os 
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
import pvporcupine as pvporcupine
import pyaudio
import struct
import time
from pipes import quote

conn = sqlite3.connect('jarvis.db')
cursor = conn.cursor()



# Play a sound file start
@eel.expose
def playAssistantSound():
    music_file = "www\\assets\\audio\\assistantvoice2.mp3"
    playsound.playsound(music_file)


def openApp(query):
    query = query.replace(Assistant_name, "")
    query = query.replace("open", "")

    query = query.strip()

    if query != "":
        
        try:
            cursor.execute(f"SELECT PATH FROM sys_command WHERE name IN (?)", (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak(f"Opening {query}")
                os.startfile(results[0][0])
            
            elif len(results) == 0:
                cursor.execute(f"SELECT url FROM web_command WHERE name IN (?)", (query,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak(f"Opening {query}")
                    webbrowser.open(results[0][0])
                else:
                    speak(f"Opening {query}")
                    try:
                        os.system(f'start {query}')
                    except:
                        speak(f"Sorry, I couldn't find the application or website named {query} in my database.")

        except Exception as e:
            print(e)
            speak("Something Went Wrong..")



def playYoutube(query):
    search_term = extract_yt_term(query)
    speak(f"Playing {search_term} on YouTube")
    kit.playonyt(search_term)
        

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"], sensitivities=[0.9, 0.9]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
            

 # Finding contacts
def findContact(query):
    
    
    words_to_remove = [Assistant_name, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('I dont know this contact there is no one in my database.')
        return 0, 0
           


def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 19
        jarvis_message = "message send successfully to "+name

    elif flag == 'whatsapp call':
        target_tab = 14
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 13
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')
   

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
        

    pyautogui.hotkey('enter')
    speak(jarvis_message)