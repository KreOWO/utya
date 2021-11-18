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

from opts import say
from callback import callback

webbrowser.register('opera-gx', None, webbrowser.BackgroundBrowser('C:\\Users\\kiril\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'))
name_sayed = True

r = sr.Recognizer()
micro = sr.Microphone(device_index = 1)
speak_engine = pyttsx3.init()
r.pause_threshold = 0.5
r.dynamic_energy_threshold = False
r.energy_threshold = 200

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
	except sr.RequestError:
		print('[log] Проверьте интернет соединение!')
	time.sleep(1)