from time import sleep
from datetime import datetime
from threading import Thread
import win32com.client as wincl

def hook_time():
    while True:
        do = True
        f = open('time_hooks.txt', 'r', encoding='utf-8')
        read_f = f.read().split('\n')
        f.close()
        if read_f != ['']:
            read_f.sort()
            for i in read_f:
                if i != '':
                    time_flag, msg = i.split('!')
                    need_time = list(map(int, time_flag.split(':')))
                    t_now = datetime.now().time()
                    if [t_now.hour, t_now.minute] == need_time:
                        fw = open('time_hooks.txt', 'w', encoding='utf-8')
                        for j in read_f:
                            if j != i:
                                fw.write(j + '\n')
                        fw.close()
                        while do:
                            say(time_flag + ' ' + msg)
                            do = False
                            sleep(1)
        sleep(30)

def say(txt):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Rate = 1
    speak.Volume = 100
    saying = lambda: speak.Speak(txt)
    print(txt)
    th = Thread(target=saying)
    th.start()
