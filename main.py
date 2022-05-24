"""

Utya voice manager 

Author of main code: KreOWO (https://github.com/KreOWO)

Authors of imported libs seen on this libs

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


class varable(object):
    name_said = True
    long_text = False
    last_text = []
    last_task = []
    last_calculated = 0

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
        varable = callback(voice, varable)
    except Exception as e:
        print(f'[ERROR] {e}')
        print('[log] Голос не распознан!')
