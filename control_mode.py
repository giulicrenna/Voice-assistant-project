from progress import bar
import speech_recognition as sr
import pyttsx3
import os
import time
import sys
import random
import re
import unidecode
from modules import driver
from modules.ex_handler import error_log
from progress.bar import ChargingBar
from modules.reader import reader


engine = pyttsx3.init()
voices = engine.getProperty('voices')
recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        with ChargingBar('Ajustando ruido del ambiente >>', max=100) as bar:
            for i in range(100):
                time.sleep(0.1)
                bar.next()
            recognizer.dynamic_energy_threshold = False
            recognizer.adjust_for_ambient_noise(source, duration=6)
            recorded_audio = recognizer.listen(source)
    os.system('color 1f')
    os.system('cls')
except Exception as error:
    print('hola')
    str(error).join(' Control mode error')
    error_log(error)

def control_orders():
    try:
        with sr.Microphone() as source:
            recorded_audio = recognizer.listen(source)
    except Exception as ex:
        print(ex)
        error_log(ex)
        control_orders()
    try: #main orders
        order_ = recognizer.recognize_google(recorded_audio, language="es-Es")
        order_ = re.sub(r'[^\w\s]', '', str(order_))  #Mistake was not converting the order from a list  to a string
        order = order_.lower()
        order = unidecode.unidecode(order)
        for i in reader('opto1.txt'):
            if i in order:
                try:
                    engine.say('Prendiendo relé uno')
                    engine.runAndWait()
                    driver.controller('ON1')
                except Exception as ex:
                    error_log(ex)
        for i in reader('opto2.txt'):
            if i in order:
                try:
                    engine.say('Prendiendo relé dos')
                    engine.runAndWait()
                    driver.controller('ON2')
                except Exception as ex:
                    error_log(ex)
        for i in reader('opto1_off.txt'):
            if i in order:
                try:
                    engine.say('Apagando relé uno')
                    engine.runAndWait()
                    driver.controller('OFF1')
                except Exception as ex:
                    error_log(ex)
        for i in reader('opto2_off.txt'):
            if i in order:
                try:
                    engine.say('Apagando relé dos')
                    engine.runAndWait()
                    driver.controller('OFF2')
                except Exception as ex:
                    error_log(ex)
        for i in reader('close.txt'):
            if i in order:
                os.system('cls')
                pre_build = open(os.getcwd() + r'\libs\pre_build_sentences.txt')
                sentence = pre_build.readlines()
                sentence = sentence[random.randint(19, 25)]
                engine.say(sentence)
                engine.runAndWait()
                sys.exit()
    except Exception as error:
        str(error).join(' Control mode error')
        error_log(error)
        control_orders()


while 1:
    control_orders()
    os.system('cls')