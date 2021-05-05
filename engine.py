import speech_recognition as sr
import pyttsx3
import subprocess
import os
import sys
import time
from opener import *
from notes import *
import random
from modules import *
import enviroment

n = random.randint(140,160)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', n) 
engine.setProperty('volume', 1) 
#engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')

recognizer = sr.Recognizer()

owner = 'giuli'

actual_path = os.getcwd()






def error_log(exception_):
    named = time.localtime() 
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs' # to logs folder
    file_name = 'error_log_%s.txt'%time_string
    file = os.path.join(path, file_name)
    file = open(file, "a") # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file 
    file.close()
def ambient_adjustement():
    with sr.Microphone() as source:
        recognizer.dynamic_energy_threshold = False
        #print(actual_path)
        pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
        sentences = pre_build.readlines()
        sentence = sentences[random.randint(2,5)]
        print(sentence)
        engine.say(sentence)         # Implement pre build sentences
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source, duration=2)
def cleaner():
    os.system('cls')
##########___________ORDERS___________#############
def _orders_():
    with sr.Microphone() as source:
        recorded_audio = recognizer.listen(source, timeout=200)
    try:
        text = recognizer.recognize_google(recorded_audio, language="es-Es")
        order_ = text.split(" ")
        order = [x.lower() for x in order_]
        #print(order)
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
            elif 'word' in order:
                engine.say('Abriendo word')
                engine.runAndWait()
                word.open()
                cleaner()
            elif 'visual' and 'studio' in order:
                engine.say('Abriendo visual studio code')
                engine.runAndWait()
                vs.open()
                cleaner()
            elif 'spotify' in order:
                engine.say('Abriendo Spotify')
                engine.runAndWait()
                spotify.open()
                cleaner()
            elif 'eclipse' in order:
                engine.say('Abriendo eclipse')
                engine.runAndWait()
                eclipse.open()
        elif "cerrar" in order:
            engine.say('Adios')
            engine.runAndWait()
            sys.exit()
        elif "adiós" in order:
            engine.say('Adios')
            engine.runAndWait()
            sys.exit()
        elif "nos" and "vemos" in order:
            engine.say('Adios')
            engine.runAndWait()
            sys.exit()
        elif ["hacer", "anotación"] == order:
            engine.say('Abriendo anotador')
            engine.runAndWait()
            engine.say('Escriba el nombre de la nota')
            engine.runAndWait()
            name_ = input('>> ')
            engine.say('Escriba la nota')
            engine.runAndWait()
            note_ = input('>> ')
            new_note = Notes(note_, name_, 1)
            new_note.add_note()
            engine.say('Nota agregada exitosamente')
            engine.runAndWait()
        elif ["eliminar", "anotacion"] == order:
            engine.say('Escriba el id de la nota a borrar')
            engine.runAndWait()
            id_ = input('>> ')
            erase_note = Notes('', '', id_) 
            erase_note.erase_notes()
            engine.say('Anotación borrada exitosamente')
            engine.runAndWait()        
        elif ["eliminar", "todas", "las", "anotaciones"] == order:
            engine.say('Escriba si, si estás seguro de elimiar todo')
            engine.runAndWait()
            print('Escriba si, si estás seguro de elimiar todo')
            bool = input('>> ')
            bool.lower()
            if bool == 'si':
                erase_all = Notes('', '', '')
                erase_all.erase_all()
                engine.say('Notas borradas con éxito')
                engine.runAndWait()
            elif bool == 'no':
                engine.say('Saliendo de notas')
                engine.runAndWait()
                initial_voice()
            else:
                engine.say('argumento incorrecto')
                engine.runAndWait()
                initial_voice()
        elif ['mostrar', "todas", "las", "anotaciones"] == order:
            engine.say('Mostrando todas las notas')
            engine.runAndWait()
            all_notes = Notes('', '', '')
            all_notes.show_notes()
            print('Presiona enter para salir. ')
            input('>> ')
        elif "ayudas" in order:
            engine.say('Mostrando ayudas')
            engine.runAndWait()
            help_ = open(os.getcwd() + r'\libs\help.txt')
            help_text = help_.read()
            print(help_text)
            print('Press Enter to quit')
            input()
        elif "ayuda" in order:
            engine.say('Mostrando ayudas')
            engine.runAndWait()
            help_ = open(os.getcwd() + r'\libs\help.txt')
            help_text = help_.read()
            print(help_text)
            print('Press Enter to quit')
            input()
        elif 'buscar' in order:
            if len(order) == 2:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch1(order[1])
                search.search()
            elif len(order) == 3:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch2(order[1], order[2])
                search.search()
            elif len(order) == 4:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch3(order[1], order[2], order[3])
                search.search()
            elif len(order) == 5:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch4(order[1], order[2], order[3], order[4])
                search.search()
            elif len(order) == 6:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch5(order[1], order[2], order[3], order[4], order[5])
                search.search()
            elif len(order) == 7:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch6(order[1], order[2], order[3], order[4], order[5], order[6])
                search.search()
            elif len(order) == 8:
                engine.say('buscando')
                engine.runAndWait()
                search = Argsearch7(order[1], order[2], order[3], order[4], order[5], order[6], order[7])
                search.search()
        elif "chiste" or "broma" in order:
            jk = open(os.getcwd() + r'\libs\jks.txt')
            jk_read = jk.readlines(random.randrange(0,8))
            #str(jk_read).lstrip()
            print(jk_read)
            engine.say(jk_read)
            engine.runAndWait()
    except Exception as ex:
        error_log(ex)
        _welcome_()
def initial_voice():   
    pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
    sentences = pre_build.readlines()
    sentence = sentences[random.randint(11,13)]
    engine.say(sentence)   # Implement pre build sentences
    print(sentence)
    engine.runAndWait() 
    while 1:                                         
        _orders_()    
        os.system('cls')
def _welcome_():                                                            #FUNCIÓN DE LOOP PARA INICIAR EL ASISTENTE AL DECIR "ABRIR"
    with sr.Microphone() as source:
        try:
            recognizer.dynamic_energy_threshold = False
            recognizer.adjust_for_ambient_noise(source, duration=1)
            initial_audio = recognizer.listen(source, timeout=6)        
        except Exception as ex:
            error_log(ex)
            _welcome_()
        try:
            open_command = recognizer.recognize_google(initial_audio, language="es-ES")
            ls_ = open_command.split(" ")
            ls = [x.lower() for x in ls_]
            #print(ls)
            if 'abrir' or 'abrite' in ls:
                ambient_adjustement()
                initial_voice()
            elif 'iniciar' or 'iniciate' in ls:
                ambient_adjustement()
                initial_voice()
            elif 'hola' in ls:
                ambient_adjustement()
                initial_voice()
        except Exception as ex:
            error_log(ex)
            _welcome_()
while 1:
    _welcome_()
    enviroment.enviroment()
