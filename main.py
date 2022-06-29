"""

Utya voice manager 

Author of main code: KreOWO (https://github.com/KreOWO)

Authors of imported libs seen on this libs

"""
import speech_recognition as sr
import webbrowser
import wave
from threading import Thread
from datetime import datetime
import pyaudio
import audioop
import math

from asyncs import say
from asyncs import hook_time
from callback import callback
from process import get_volume

const = {
    'CHUNK': 4096,
    'FORMAT': pyaudio.paInt16,
    'CHANNELS': 1,
    'RATE': 42100,
    'DEVICE': 1,
    'RECORD_SECONDS': 10,
    'SH_TIME': 0.5,
    'SHH': True,
    'WAVE_OUTPUT_FILENAME': "output.wav",
    'INGNORE_EXCEPTIONS': True,
}


class varable(object):
    name_said = True
    long_text = False
    last_text = []
    last_task = []
    last_calculated = 0
    last_volume = get_volume()


def recognize(varable):
    r = sr.Recognizer()
    sample = sr.WavFile('output.wav')
    with sample as audio:
        content = r.record(audio)
        r.adjust_for_ambient_noise(audio)
    
    if not const['INGNORE_EXCEPTIONS']:
        voice = r.recognize_google(content, language='ru-RU').lower()
        print('[log] Распознано: ' + voice)
        varable = callback(voice, varable)
    else:
        try:
            voice = r.recognize_google(content, language='ru-RU').lower()
            print('[log] Распознано: ' + voice)
            varable = callback(voice, varable)
        except Exception as e:
            print(f'[ERROR] {e}')
            print('[log] Голос не распознан!')


def main():
    webbrowser.register('opera-gx', None, webbrowser.BackgroundBrowser('C:\\Users\\kiril\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'))

    hook_time_thread = Thread(target=hook_time)
    hook_time_thread.start()
    
    now = datetime.now().hour
    if now < 9:
        say('Доброе утро')
    elif now < 17:
        say('добрый день')
    else:
        say('добрый вечер')
        
    p = pyaudio.PyAudio()
    
    stream = p.open(format=const['FORMAT'],
                    channels=const['CHANNELS'],
                    rate=const['RATE'],
                    input=True,
                    frames_per_buffer=const['CHUNK'],
                    input_device_index=const['DEVICE']
                    )
    
    print('Говорите')
    
    frames = []
    count = const['RATE'] / const['CHUNK'] * const['SH_TIME']
    while True:
        data = stream.read(const['CHUNK'])
        
        rms = audioop.rms(data, 2)
        decibel = 20 * math.log10(rms)
        
        count = count * int(decibel < 25) + int(decibel < 25)
        
        if count >= const['RATE'] / const['CHUNK'] * const['SH_TIME']:
            w = wave.open(const['WAVE_OUTPUT_FILENAME'], 'wb')
            w.setnchannels(const['CHANNELS'])
            w.setsampwidth(p.get_sample_size(const['FORMAT']))
            w.setframerate(const['RATE'])
            w.writeframes(b''.join(frames))
            w.close()
            frames = []
            if not const['SHH']:
                th = Thread(target=recognize, args=[varable])
                th.start()
                const['SHH'] = True
            
        else:
            frames.append(data)
            if const['SHH']:
                const['SHH'] = False

if __name__ == '__main__':
    main()
