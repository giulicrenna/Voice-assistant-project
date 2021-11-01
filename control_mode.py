#from typing_extensions import ParamSpecKwargs
from progress import bar
import speech_recognition as sr
import os
import time
import sys
import random
import re
import beepy
import unidecode
from modules import driver
from modules.ex_handler import error_log
from progress.bar import ChargingBar
from modules.reader import reader
from modules.gtt_voice import say

recognizer = sr.Recognizer()

try:
    with sr.Microphone() as source:
        with ChargingBar('Ajustando ruido del ambiente >>', max=50) as bar:
            for i in range(50):
                time.sleep(0.1)
                bar.next()
            recognizer.dynamic_energy_threshold = False
            recognizer.adjust_for_ambient_noise(source, duration=6)
except Exception as es:
    print(es)
    time.sleep(5)

def control_orders():
    with sr.Microphone() as source:
        recorded_audio = recognizer.listen(source, timeout=50)
    try: #main orders
        order_ = recognizer.recognize_google(recorded_audio, language="es-AR")
        order_ = re.sub(r'[^\w\s]', '', str(order_))  #Mistake was not converting the order from a list  to a string
        order = order_.lower()
        order = unidecode.unidecode(order)
        for i in reader('opto1.txt'):
            if i in order:
                say('Prendiendo relé uno')
                driver.controller('ON1')
                break
        for i in reader('opto1_off.txt'):
            if 'apagar' and '1' in order:
                say('Apagando relé uno')
                driver.controller('OFF1')
                break   
        for i in reader('opto2.txt'):
            if i == order:
                say('Prendiendo relé dos')
                driver.controller('ON2')
                break
        for i in reader('opto2_off.txt'):
            if 'apagar' and '2' in order:
                say('Apagando relé dos')
                driver.controller('OFF2')
                break
        for i in reader('close.txt'):
            if i in order:
                os.system('clear')
                pre_build = open(os.getcwd() + r'/libs/pre_build_sentences.txt')
                sentence = pre_build.readlines()
                sentence = sentence[random.randint(19, 25)]
                say(sentence)
                sys.exit()
    except Exception as error:
        str(error).join(' Control mode error')
        error_log(error)
        control_orders()

def trigger():
    with sr.Microphone() as source:
        try:
            initial_audio = recognizer.listen(source, timeout=50)
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
                    control_orders()
                    break
        except Exception as ex:
            error_log(ex)
            pass

while 1:
    os.system('clear')
    trigger()
    