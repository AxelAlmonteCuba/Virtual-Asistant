import os
import subprocess as sub
from tkinter import *
from virtual_assistant import *

main_window = Tk()
main_window.title("Dino")

main_window.geometry("800x450")
main_window.resizable(0, 0)
main_window.configure(bg='#00B4DB')

text_info = Text(main_window, bg="#00B4DB", fg="black")
text_info.place(x=0, y=170, height=280, width=198)
def escribe(rec):
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

    f.write(rec_write + os.linesep)
    f.close()
    speak("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)            

