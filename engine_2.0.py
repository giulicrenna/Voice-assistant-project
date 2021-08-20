import speech_recognition as sr
import pyttsx3
import os
import sys
import time
import re
import unidecode 
from modules import opener
from modules import notes
from modules import ex_handler
from modules import reader
from modules.reader import reader
from modules.search import *
from modules import climate
from modules import driver
from modules import jokes
import random
#import subprocess

owner = 'giuli'



n = random.randint(140, 160)

actual_path = os.getcwd()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', n)
engine.setProperty('volume', 1)
recognizer = sr.Recognizer()

def cleaner():
    os.system('cls')

def ambient_adjustement():
    with sr.Microphone() as source:
        recognizer.dynamic_energy_threshold = False
        # print(actual_path)
        pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
        sentences = pre_build.readlines()
        sentence = sentences[random.randint(2, 5)]
        print(sentence)
        engine.say(sentence)         # Implement pre build sentences
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source, duration=2)

def list_to_str(list_):
    empty = ""
    for i in list_:
        empty += i
    return empty

def _orders_():
    try:
        with sr.Microphone() as source:
            recorded_audio = recognizer.listen(source)
    except Exception as ex:
        print(ex)
        ex_handler.error_log(ex)
        _orders_()
    try:
        cleaner()
        order_ = recognizer.recognize_google(recorded_audio, language="es-Es")
        order_ = re.sub(r'[^\w\s]', '', str(order_))  #Mistake was not converting the order from a list  to a string
        order = order_.lower()
        order = unidecode.unidecode(order)
        for i in reader('insult.txt'):
            if i in order:
                engine.say("callate puto de mierda")
                engine.runAndWait()
                break
            else:
                pass
        for i in reader('close.txt'):
            if i in order:
                cleaner()
                pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
                sentence = pre_build.readlines()
                sentence = sentence[random.randint(19, 25)]
                engine.say(sentence)
                engine.runAndWait()
                sys.exit()
        for i in reader('notes.txt'):  #Terminar notes
            #res = any(x in i for x in order_)
            if i in order:
                engine.say('Abriendo anotador')
                engine.runAndWait()
                engine.say('Escriba el nombre de la nota')
                engine.runAndWait()
                name_ = input('>> ')
                engine.say('Escriba la nota')
                engine.runAndWait()
                note_ = input('>> ')
                new_note = notes.Notes(note_, name_)
                new_note.add_note()
                engine.say('Nota agregada exitosamente')
                engine.runAndWait()
                cleaner()
        for i in reader('notes_delete.txt'):
            if i in order:
                engine.say('Escriba el nombre de la nota a borrar')
                engine.runAndWait()
                id_ = input('>> ')
                erase_note = notes.Notes('', id_) 
                erase_note.erase_notes()
                engine.say('Anotación borrada exitosamente')
                cleaner()
        for i in reader('notes_delete_all.txt'):
            if i in order:
                engine.say('Escriba si, si estás seguro de elimiar todo')
                engine.runAndWait()
                print('Escriba si, si estás seguro de elimiar todo')
                bool = input('>> ')
                bool.lower()
                if bool == 'si':
                    erase_all = notes.Notes('', '')
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
                cleaner()
        for i in reader('notes_show_all.txt'):
            if i in order:
                engine.say('Mostrando todas las notas')
                engine.runAndWait()
                all_notes = notes.Notes('', '')
                all_notes.show_notes()
                print('\nPresiona enter para salir. ')
                input('>> ')
                cleaner()
        for i in reader('climate.txt'):
            if i in order:
                engine.say("Por favor escribe la ciudad")
                engine.runAndWait()
                city = input(">> ")
                weather = climate.Weather(city)
                weather = weather.get_weather()
                print(weather)
                engine.say(weather)
                engine.runAndWait()
                time.sleep(3)
                cleaner()
        for i in reader('search.txt'):                       # Fix the search function
            if i in order:
                order = order.replace('de', '', 1)
                order = order.replace('es', '', 1)
                order = order.split()
                try:
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
                except Exception as e:
                    engine.say('Lo siento, pero no se puede realizar la búsqueda...')
                    engine.runAndWait()
                    ex_handler.error_log(e)
        for i in reader('opto1.txt'):
            if i in order:
                try:
                    engine.say('Prendiendo relé uno')
                    engine.runAndWait()
                    driver.controller('ON1')
                except Exception as ex:
                    ex_handler.error_log(ex)
        for i in reader('opto2.txt'):
            if i in order:
                try:
                    engine.say('Prendiendo relé dos')
                    engine.runAndWait()
                    driver.controller('ON2')
                except Exception as ex:
                    ex_handler.error_log(ex)
        for i in reader('opto1_off.txt'):
            if i in order:
                try:
                    engine.say('Apagando relé uno')
                    engine.runAndWait()
                    driver.controller('OFF1')
                except Exception as ex:
                    ex_handler.error_log(ex)
        for i in reader('opto2_off.txt'):
            if i in order:
                try:
                    engine.say('Apagando relé dos')
                    engine.runAndWait()
                    driver.controller('OFF2')
                except Exception as ex:
                    ex_handler.error_log(ex)
        for i in reader('jokes.txt'):
            if i in order:
                num = random.randint(1, 23)
                string = jokes.jokes(num)
                print(string)
                engine.say(string)
                engine.runAndWait()
                time.sleep(2)

    except Exception as ex:
        ex_handler.error_log(ex)
        _orders_()

def initial_voice():
    pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
    sentences = pre_build.readlines()
    sentence = sentences[random.randint(11, 13)]
    engine.say(sentence)   # Implement pre build sentences
    print(sentence)
    engine.runAndWait()
    while 1:
        _orders_()
        os.system('cls')


def _welcome_():  # FUNCIÓN DE LOOP PARA INICIAR EL ASISTENTE AL DECIR "ABRIR"
    with sr.Microphone() as source:
        try:
            os.system('cls')
            recognizer.dynamic_energy_threshold = False
            print('Ajustando ruido del ambiente')
            recognizer.adjust_for_ambient_noise(source, duration=3)
            print('\nListo!\n')
        except Exception as ex:
            ex_handler.error_log(ex)
            _welcome_()
        def recong():
            try:
                initial_audio = recognizer.listen(source, timeout=50)
                open_command = recognizer.recognize_google(
                    initial_audio, language="es-ES")  # Recognized text
                open_command = re.sub(r'[^\w\s]', '', str(open_command)) # this line delete all quotation marks
                order = open_command.lower()
                order = unidecode.unidecode(order)
                order = order.split(' ')
                for i in reader('init.txt'):
                    i = str(i).split(' ')
                    res = any(item in i for item in order)
                    if res == True:
                        ambient_adjustement()
                        initial_voice()
            except Exception as ex:
                ex_handler.error_log(ex)
                recong()
        recong()

_welcome_()


#add radio station
# Remember to compare the order (a string) with
# reader_ (a list), and create a .txt per function