import speech_recognition as sr
import pyttsx3
import subprocess
import os
import sys
import time
from opener import *
#from notes import *
import random
from modules.search import *
import re
from unidecode import unidecode 

n = random.randint(140, 160)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', n)
engine.setProperty('volume', 1)
recognizer = sr.Recognizer()

owner = 'giuli'

actual_path = os.getcwd()


def error_log(exception_):
    named = time.localtime()
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs'  # to logs folder
    file_name = 'error_log_%s.txt' % time_string
    file = os.path.join(path, file_name)
    file = open(file, "a")  # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file
    file.close()


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


def cleaner():
    os.system('cls')


def reader(file):
    file_ = open(r'orders/{}'.format(file), 'r')
    line = file_.readlines()
    line = list(map(lambda l: l.rstrip('\n'), line)) #This line strip all \n in the element from the list
    return line




def _orders_():
    with sr.Microphone() as source:
        recorded_audio = recognizer.listen(source, timeout=5)
    try:
        order_ = recognizer.recognize_google(recorded_audio, language="es-Es")
        order_ = re.sub(r'[^\w\s]', '', str(order_))  #Mistake was not converting the order from a list  to a string
        order = order_.lower()
        print(order)
        for i in reader('insult.txt'):
            if i in order:
                engine.say("callate puto de mierda")
                engine.runAndWait()
                break
            else:
                pass


    except Exception as ex:
        error_log(ex)
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
            print('\nListo!')
            initial_audio = recognizer.listen(source, timeout=10)
        except Exception as ex:
            error_log(ex)
            _welcome_()
        try:
            open_command = recognizer.recognize_google(
                initial_audio, language="es-ES")  # Recognized text
            open_command = re.sub(r'[^\w\s]', '', str(open_command)) # this line delete all quotation marks
            #ls_ = open_command.split(" ")  # Creates a list
            order = open_command.lower()
            #unidecode.unidecode(order)
            print(order)
            reader_ = reader('init.txt')
            if order in reader_:
                ambient_adjustement()
                initial_voice()
        except Exception as ex:
            error_log(ex)
            _welcome_()


while 1:
    _welcome_()



# Remember to compare the order (a string) with
# reader_ (a list), and create a .txt per function