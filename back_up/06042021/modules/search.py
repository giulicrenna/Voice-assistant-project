import wikipedia as wk
import os, sys
import time
import pyttsx3

class Argsearch1:
    def __init__(self, arg):
        self.arg = arg
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg, sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch2:
    def __init__(self, arg, arg2):
        self.arg = arg
        self.arg2 = arg2
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2, 
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch3:
    def __init__(self, arg, arg2, arg3):
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2 + ' ' + self.arg3,
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch4:
    def __init__(self, arg, arg2, arg3, arg4):
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2 + ' ' + self.arg3 + ' ' + self.arg4,
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch5:
    def __init__(self, arg, arg2, arg3, arg4, arg5):
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2 + ' ' + self.arg3 + ' ' + self.arg4 + ' ' + self.arg5,
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch6:
    def __init__(self, arg, arg2, arg3, arg4, arg5, arg6):
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        self.arg6 = arg6
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2 + ' ' + self.arg3 + ' ' + self.arg4 + ' ' + self.arg5 + ' ' + self.arg6,
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)

class Argsearch7:
    def __init__(self, arg, arg2, arg3, arg4, arg5, arg6, arg7):
        self.arg = arg
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        self.arg6 = arg6
        self.arg7 = arg7
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg + ' ' + self.arg2 + ' ' + self.arg3 + ' ' + self.arg4 + ' ' + self.arg5 + ' ' + self.arg6 + ' ' + self.arg7,
            sentences=7)
            print(inf)
            engine = pyttsx3.init()
            engine.say(inf)
            #engine.runAndWait()
            input()
        except:
            print('No hay coincidencia de busqueda')
            time.sleep(4)


