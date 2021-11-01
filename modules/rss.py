import feedparser
import os
from modules import ex_handler
from modules.gtt_voice import say

path = os.getcwd()
path = os.path.join(path, "modules", "config.txt")
config = open(path, "rt")
url = config.readlines()

last = str(url[7])
politics = str(url[8])
world = str(url[9])

def rss_last():
    try:
        feed = feedparser.parse(last)
        lenght = len(feed.entries)
        for entry in range(lenght):
            text = feed.entries[entry]
            print(text.summary)
            say(text.summary)
    except KeyboardInterrupt:
        ex_handler.error_log("Keyboard interruption")
        pass

def rss_politics():
    try:
        feed = feedparser.parse(politics)
        lenght = len(feed.entries)
        for entry in range(lenght):
            text = feed.entries[entry]
            print(text.summary)
            say(text.summary)
    except KeyboardInterrupt:
        ex_handler.error_log("Keyboard interruption")
        pass

def rss_world():
    try:
        feed = feedparser.parse(world)
        lenght = len(feed.entries)
        for entry in range(lenght):
            text = feed.entries[entry]
            print(text.summary)
            say(text.summary)
    except KeyboardInterrupt:
        ex_handler.error_log("Keyboard interruption")
        exit()
