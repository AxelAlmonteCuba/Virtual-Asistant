import os

import time
import pyautogui
import speech_recognition as sr


def get_audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f" Escuchando...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
                     
            rec = rec.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            status = True        
        except:
            pass
    return {'text':rec, 'status':status}

signos = {
  "mas" : "add",
  "menos" : "-",
  "entre" : "/",
  "por" : "*" 
}

os.system("calc.exe")
ecuacioon = get_audio()
ecuacioon   = ecuacioon['text']
array1 = ecuacioon.split()
time.sleep(2)

for num in array1:
  try:
    num = int(num)
  except:
    num = signos[num]
  num = str(num)  
  print(num)
  pyautogui.press(num)  
pyautogui.press("enter")  

