import os
import subprocess
import sys

class opener:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name

    def open(self):
        subprocess.Popen(self.directory)
        print('Abriendo ' + self.name)

chrome = opener(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', 'Google Chrome')
vs = opener(r'C:\Users\Giuliano\AppData\Local\Programs\Microsoft VS Code\code.exe', 'Visual Studio Code')
eclipse = opener(r'C:\Program Files\Eclipse\eclipse\eclipse.exe', 'Eclipse')
spotify = opener(r'C:\Users\Giuliano\AppData\Roaming\Spotify\Spotify.exe', 'Spotify')
word = opener (r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.exe', 'Word')
excel = opener(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.exe', 'Excel')
configuraciones = opener(r'C:\WINDOWS\System32', 'Configuraciones')
photoshop = opener(r'C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe', 'Photoshop')
notepad = opener(r'C:\Program Files\Windows NT\Accessories\wordpad.exe', 'Notepad')