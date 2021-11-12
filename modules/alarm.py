import argparse
import os
import time


path = os.getcwd()
path = os.path.join(path, "modules", "config.txt")
config = open(path, "rt")
ringtone = config.readlines()


parser = argparse.ArgumentParser()
parser.add_argument('-j', '--hour')
parser.add_argument('-m', '--minute')
parser.add_argument('-s', '--seconds')
arguments = parser.parse_args()

def hour_to_segs(hour):
    sgs = hour * 60 * 60

    return sgs

def min_to_segs(min):
    sgs = min * 60

    return sgs


total_time = 0
if arguments.hour:
    total_time += hour_to_segs(int(arguments.hour))
if arguments.minute:
    total_time += min_to_segs(int(arguments.minute))
if arguments.seconds:
    total_time += int(arguments.seconds)

time.sleep(total_time) 
os.system('mp3-decoder -q libs/sounds/{}.mp3'.format(ringtone[11]))

