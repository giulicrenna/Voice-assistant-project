import speech_recognition as sr
import os
import sys
import time
import re
import unidecode
import random
import beepy
from modules import notes
from modules import ex_handler
from modules import reader
from modules.reader import reader
from modules.search import *
from modules import climate
from modules import jokes
from progress.bar import ChargingBar
from modules.gtt_voice import say
from modules import rss

owner = 'giuli'

n = random.randint(140, 160)

actual_path = os.getcwd()

recognizer = sr.Recognizer()

def cleaner():
    os.system('clear')

def ambient_adjustement():
    say('Ajustando ruido del ambiente')
    
    with sr.Microphone() as source:
        with ChargingBar('Ajustando ruido del ambiente >>', max=20) as bar:
            for i in range(20):
                time.sleep(0.1)
                bar.next()
            recognizer.dynamic_energy_threshold = False
            recognizer.adjust_for_ambient_noise(source, duration=6)
            pre_build = open(os.getcwd() + r'/libs/pre_build_sentences.txt')
            sentences = pre_build.readlines()
            sentence = sentences[random.randint(2, 5)]
            print('\n{}'.format(sentence))
            say(sentence)         # Implement pre build sentences
            
            
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
        pass
    try:
        cleaner()
        order_ = recognizer.recognize_google(recorded_audio, language="es-AR")
        order_ = re.sub(r'[^\w\s]', '', str(order_))  #Mistake was not converting the order from a list  to a string
        order = order_.lower()
        order = unidecode.unidecode(order)
        print(order)
        for i in reader('insult.txt'):
            if i in order:
                say("callate puto de mierda")
                
                break
            else:
                pass
        for i in reader('close.txt'):
            if i in order:
                cleaner()
                pre_build = open(os.getcwd() + r'/libs/pre_build_sentences.txt')
                sentence = pre_build.readlines()
                sentence = sentence[random.randint(19, 25)]
                say(sentence)
                
                os.system('shutdown')
        for i in reader('notes.txt'):  #Terminar notes
            #res = any(x in i for x in order_)
            if i in order:
                say('Abriendo anotador')
                
                say('Escriba el nombre de la nota')
                
                name_ = input('>> ')
                say('Escriba la nota')
                
                note_ = input('>> ')
                new_note = notes.Notes(note_, name_)
                new_note.add_note()
                say('Nota agregada exitosamente')
                
                cleaner()
        for i in reader('notes_delete.txt'):
            if i in order:
                say('Escriba el nombre de la nota a borrar')
                
                id_ = input('>> ')
                erase_note = notes.Notes('', id_) 
                erase_note.erase_notes()
                say('Anotación borrada exitosamente')
                cleaner()
        for i in reader('notes_delete_all.txt'):
            if i in order:
                say('Escriba si, si estás seguro de elimiar todo')
                
                print('Escriba si, si estás seguro de elimiar todo')
                bool = input('>> ')
                bool.lower()
                if bool == 'si':
                    erase_all = notes.Notes('', '')
                    erase_all.erase_all()
                    say('Notas borradas con éxito')
                    
                elif bool == 'no':
                    say('Saliendo de notas')
                    
                else:
                    say('argumento incorrecto')
                    
                cleaner()
        for i in reader('notes_show_all.txt'):
            if i in order:
                say('Mostrando todas las notas')
                all_notes = notes.Notes('', '')
                all_notes.show_notes()
                print('\nPresiona enter para salir. ')
                input('>> ')
                cleaner()
        for i in reader('climate.txt'):
            if i in order:
                path = os.getcwd()
                path = os.path.join(path, "modules", "config.txt")
                config = open(path, "rt")
                city = config.readlines()
                city = str(city[5])

                weather = climate.Weather(city)
                weather = weather.get_weather()

                print(weather)
                say(weather)
                time.sleep(3)
                cleaner()

        for i in reader('search.txt'):                       
            if i in order:
                order = order.replace('de', '', 1)
                order = order.replace('es', '', 1)
                order = order.split()
                try:
                    if len(order) == 2:
                        say('buscando')
                        search = Argsearch1(order[1])
                        search.search()
                    elif len(order) == 3:
                        say('buscando')
                        search = Argsearch2(order[1], order[2])
                        search.search()
                    elif len(order) == 4:
                        say('buscando')                       
                        search = Argsearch3(order[1], order[2], order[3])
                        search.search()
                    elif len(order) == 5:
                        say('buscando')                       
                        search = Argsearch4(order[1], order[2], order[3], order[4])
                        search.search()
                    elif len(order) == 6:
                        say('buscando')                        
                        search = Argsearch5(order[1], order[2], order[3], order[4], order[5])
                        search.search()
                    elif len(order) == 7:
                        say('buscando')                
                        search = Argsearch6(order[1], order[2], order[3], order[4], order[5], order[6])
                        search.search()
                    elif len(order) == 8:
                        say('buscando')
                        search = Argsearch7(order[1], order[2], order[3], order[4], order[5], order[6], order[7])
                        search.search()
                except Exception as e:
                    say('Lo siento, pero no se puede realizar la búsqueda...')
                    
                    ex_handler.error_log(e)
                break
        for i in reader('control_mode.txt'):
            if i in order:
                say('Iniciando modo controlador')
                try:
                    path = os.getcwd()
                    path = os.path.join(path, 'control_mode.py')
                    os.system('python3.9 {}'.format(path))
                    exit()
                except Exception as e:
                    ex_handler.error_log(e)
        for i in reader('jokes.txt'):
            if i in order:
                num = random.randint(1, 23)
                string = jokes.jokes(num)
                print(string)
                say(string)
                break
                
                time.sleep(2)
        for i in reader('rss.txt'):
            if i and 'globales' in order:
                rss.rss_world()
                break
            if i and 'actuales' in order:
                rss.rss_last()
                break
            if i and 'politica' in order:
                rss.rss_politics()
                break
        for i in reader('alarm.txt'):
            if i in order:
                os.system('python3.9 modules/alarm.py &')
            break
    except Exception as ex:
        ex_handler.error_log(ex)
        pass


def trigger():  # FUNCIÓN DE LOOP PARA INICIAR EL ASISTENTE AL DECIR "ABRIR"
    with sr.Microphone() as source:
        def recong():
            try:
                initial_audio = recognizer.listen(source, timeout=5)
                open_command = recognizer.recognize_google(
                    initial_audio, language="es-AR")  # Recognized text
                open_command = re.sub(r'[^\w\s]', '', str(open_command)) # this line delete all quotation marks
                order = open_command.lower()
                order = unidecode.unidecode(order)
                order = order.split(' ')
                
                for i in reader('init.txt'):
                    i = str(i).split(' ')
                    res = any(item in i for item in order)
                    if res == True:
                        beepy.beep(sound=5)
                        _orders_()
                        break
            except Exception as ex:
                ex_handler.error_log(ex)
                pass
        recong()


ambient_adjustement()
time.sleep(3)
while True:
    trigger()



#add radio station
# Remember to compare the order (a string) with
# reader_ (a list), and create a .txt per function