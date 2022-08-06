import AVMSpeechMath as sm
import AVMYT as yt
from exceptiongroup import catch
import spoty
import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
from datetime import datetime, date, timedelta
import wikipedia
import pyjokes
from time import time
from SpotyP import *
from clima import *
import os
import subprocess as sub
from tkinter import *

start_time = time()
engine = pyttsx3.init()

# name of the virtual assistant
name = 'dino'
attemts = 0
    
    
with open('version_2.0\\virtual_assistant\\keys.json') as file:
    keys = json.load(file)

#notas
main_window = Tk()
main_window.title("Dino")

main_window.geometry("800x450")
main_window.resizable(0, 0)
main_window.configure(bg='#00B4DB')

text_info = Text(main_window, bg="#00B4DB", fg="black")
text_info.place(x=0, y=170, height=280, width=198)


# colors
#

green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

day_es = [line.rstrip('\n') for line in open('version_2.0\\virtual_assistant\\src\\day\\day_es.txt')]
day_en = [line.rstrip('\n') for line in open('version_2.0\\virtual_assistant\\src\\day\\day_en.txt')]

def iterateDays(now):  
    for i in range(len(day_en)):        


        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

def getDaysAgo(rec):
    value =""
    if 'ayer' in rec:
        days = 1
        value = 'ayer'
    elif 'antier' in rec:
        days = 2
        value = 'antier'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                break
            except:
                pass
    
    if days != 0:
        try:
            now = date.today() - timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()

            if value != "":
                return f"{value} fue {iterateDays(now)}"
            else:
                return f"Hace {days} días fue {iterateDays(now)}"
        except:
            return "Aún no existíamos"
    else:
        return "No entendí"

def writer():
    try:
        with open("nota.txt", 'a') as f:
            write(f)

    except FileNotFoundError as e:
        file = open("nota.txt", 'a')
        write(file)
def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

def write(f):
    speak("¿Qué quieres que escriba?")
    rec_write = get_audio(0)
    rec_write = rec_write['text']
    f.write(rec_write + os.linesep)
    f.close()
    speak("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)            




def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio(statuds):
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"{green_color}({attemts}) Escuchando...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            print(rec)
            if statuds == 1:
                if name in rec:
                    rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                    status = True
                else:
                    print(f"Vuelve a intentarlo, no reconozco: {rec}")
            else:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True        
        except:
            pass
    return {'text':rec, 'status':status}

while True:
    rec_json = get_audio(1)

    rec = rec_json['text']
    status = rec_json['status']

    if status:
        if 'estas ahi' in rec:
            speak('Por supuesto')

        elif 'reproduce' in rec:
            if 'spotify' in rec:
                music = rec.replace('reproduce en spotify', '')
                Spitify_play("",music)                                             
                                
            else:
                music = rec.replace('reproduce', '')
                speak(f'Reproduciendo {music}')
                pywhatkit.playonyt(music)
                # yt.play(music)

        elif 'cuantos suscriptores tiene' in rec:
            name_subs = rec.replace('cuantos suscriptores tiene', '')
            
            speak("Procesando...")
            while True:
                try:
                    channel = yt.getChannelInfo(name_subs)
                    speak(channel["name"] + " tiene " + channel["subs"])
                    break
                except:
                    speak("Volviendo a intentar...")
                    continue

        elif 'que' in rec:
            if 'hora' in rec:
                hora = datetime.now().strftime('%I:%M %p')
                speak(f"Son las {hora}")

            elif 'dia' in rec:
                if 'fue' in rec:
                    speak(f"{getDaysAgo(rec)}")
                else:
                    speak(f"Hoy es {getDay()}")

        elif 'busca' in rec:
            order = rec.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            speak(info)

        elif 'clima' in rec:
            city = rec.replace('cual es el clima de ', '')
            speak(run_mike(city))       
        
           
        elif 'chiste' in rec:
            chiste = pyjokes.get_joke("es")
            speak(chiste)

        elif 'cuanto es' in rec:
            speak(sm.getResult(rec))

        elif 'descansa' in rec:
            speak("Saliendo...")
            break

        elif 'escribe' in rec:
            writer()
        else:
            print(f"Vuelve a intentarlo, no reconozco: {rec}")
        
        attemts = 0
    else:
        attemts += 1

print(f"{red_color} PROGRAMA FINALIZADO CON UNA DURACIÓN DE: { int(time() - start_time) } SEGUNDOS {normal_color}")

