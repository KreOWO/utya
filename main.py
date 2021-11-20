"""

Utya voice manager 

Author of main code: KreOWO (https://github.com/KreOWO)

Authors of imported libs seen on this libs
"""

import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
import webbrowser
import time
import datetime
from threading import Thread

from opts import say
from callback import callback


def hook_time():
	while True:
		do = True
		f = open('time_hooks.txt', 'r', encoding = 'utf-8')
		read_f = f.read().split('\n')
		f.close()
		if read_f != ['']:
			read_f.sort()
			for i in read_f:
				if i != '':
					need_time, msg = i.split('!')
					need_time = list(map(int, need_time.split(':')))
					t_now = datetime.datetime.now().time()
					if [t_now.hour, t_now.minute] == need_time:
						fw = open('time_hooks.txt', 'w', encoding = 'utf-8')
						for j in read_f:
							if j != i: 
								fw.write(j + '\n')
						fw.close()
						while do:
							try:
								say(msg)
								do = False
							except:
								time.sleep(1)
		time.sleep(30)

webbrowser.register('opera-gx', None, webbrowser.BackgroundBrowser('C:\\Users\\kiril\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'))
name_sayed = True

r = sr.Recognizer()
micro = sr.Microphone(device_index = 1)
speak_engine = pyttsx3.init()
r.pause_threshold = 0.5
r.dynamic_energy_threshold = False
r.energy_threshold = 200

th = Thread(target = hook_time)
th.start()

say('утёнок в деле!')

while True: 
	with micro as source:
		print("Говорите")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	try:
		voice = r.recognize_google(audio, language = 'ru-RU').lower()
		print('[log] Распознано: ' + voice)
		name_sayed = callback(voice, name_sayed)
	except sr.UnknownValueError:
		print('[log] Голос не распознан!')
	except:
		print('[log] Проверьте интернет соединение!')
	time.sleep(1)
