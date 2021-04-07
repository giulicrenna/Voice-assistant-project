import speech_recognition as sr
import pyttsx3
import subprocess
import os
import sys
from opener import *

engine = pyttsx3.init() 
recognizer = sr.Recognizer()

def ambient_adjustement():
    with sr.Microphone() as source:
        recognizer.dynamic_energy_threshold = False
        print('Ajustando el ruido del ambiente')
        engine.say("Ajustando el ruido del ambiente")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source, duration=2)

def cleaner():
    os.system('cls')
    main_function()
def main_function():                                       
    with sr.Microphone() as source:
        #######################
        print('Ordeneme algo')
        engine.say("Ordeneme algo")
        engine.runAndWait()
        recorded_audio = recognizer.listen(source, timeout=200)        
    try:
        text = recognizer.recognize_google(
                recorded_audio, 
                language="es-Es"
            )
        order = text.split(" ")  # <<<< FOR SEPARATING THE WORDS INSIDE THE STRING AND CAN EVALUATE EACH ONE
        print(order)  # ELIMINATE THIS LINE, ONLY FOR DEVELOPING
##########___________ORDERS___________#############
        if 'parió' in order:
            engine.say("callate puto de mierda")
            engine.runAndWait()
            cleaner()
        elif 'abrir' in order:
            if 'notepad' in order:
                engine.say('Abriendo Notepad')
                engine.runAndWait()
                notepad.open()
                cleaner()
            elif 'photoshop' in order:
                engine.say('Abriendo Photoshop')
                engine.runAndWait()
                spotify.open()
                cleaner()
            elif 'configuraciones' in order:
                engine.say('Abriendo configuraciones')
                engine.runAndWait()
                configuraciones.open()
                cleaner()
            elif 'Word' in order:
                engine.say('Abriendo word')
                engine.runAndWait()
                word.open()
                cleaner()
    except Exception as ex:
        print(ex)


def main_loop():                                                            #FUNCIÓN DE LOOP PARA INICIAR EL ASISTENTE AL DECIR "ABRIR"
    with sr.Microphone() as source:
        try:
            recognizer.dynamic_energy_threshold = False
            recognizer.adjust_for_ambient_noise(source, duration=5)
            initial_audio = recognizer.listen(source, timeout=200)        
        except:
            main_loop()
    try:
        open_command = recognizer.recognize_google(initial_audio, language="es-ES")
        ls = open_command.split(" ")
        if 'abrir' or 'abrite' in ls:
            while 1:
                ambient_adjustement()
                main_function()
        elif 'iniciar' or 'iniciate' in ls:
            while 1:
                ambient_adjustement()
                main_function()
    except Exception as ex:
        print(ex)

main_loop()