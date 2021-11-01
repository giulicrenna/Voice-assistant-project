import wikipedia as wk
import os
import time
from modules.gtt_voice import say

def error_log2(exception_):
    named = time.localtime() 
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs' # to logs folder
    file_name = 'error_log_%s.txt'%time_string
    file = os.path.join(path, file_name)
    file = open(file, "a") # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file 
    file.close()

class Argsearch1:
    def __init__(self, arg):
        self.arg = arg
    def search(self):
        try:
            wk.set_lang('es')
            inf = wk.summary(self.arg, sentences=2)
            print(inf)
            say(inf)       
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            say(inf)
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            say(inf)
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            say(inf)
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            inf = str(inf)
            say('{}'.format(inf))
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            say(inf)
            
        except Exception as e:
            error_log2(e)
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
            sentences=2)
            print(inf)
            say(inf)
            
        except Exception as e:
            error_log2(e)
            print('No hay coincidencia de busqueda')
            time.sleep(4)

