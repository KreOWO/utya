"""

Utya voice manager 

Author of main code: KreOWO (https://github.com/KreOWO)

Authors of imported libs seen on this libs


в планах:

ещё нужно сделать такую з***** чтобы голос лучше распознавался точнее вычитать из звука с микрофона звук с компьютера

сделать так чтобы запоминал последнюю цифру посчитаю и считал от неё дальше



"""

import speech_recognition as sr
import pyttsx3
import webbrowser
from threading import Thread

from asyncs import say
from asyncs import hook_time
from callback import callback

# YOUR PATH TO OPERA launcher.exe
webbrowser.register('opera-gx', None, webbrowser.BackgroundBrowser('C:\\Users\\kiril\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'))

name_said = True
long_text = False
last_text = []

r = sr.Recognizer()
micro = sr.Microphone(device_index=1)
speak_engine = pyttsx3.init()
r.pause_threshold = 0.5

hook_time_thread = Thread(target=hook_time)
hook_time_thread.start()

say('утёнок в деле!')

while True:
    with micro as source:
        print("Говорите")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        voice = r.recognize_google(audio, language='ru-RU').lower()
        print('[log] Распознано: ' + voice)
        name_said, long_text, last_text = callback(voice, name_said, long_text, last_text)
    except Exception as e:
        print(f'[ERROR] {e}')
        print('[log] Голос не распознан!')
