import os
import datetime
import webbrowser
import win32gui
import keyboard
import mouse
import wikipedia

from asyncs import say
from process import work_process
from process import opera_work
from process import set_volume
from process import mind
from process import calculate
from process import rus_to_eng
from process import to_num
from process import get_volume


def exec_cmd(cmd, cmd_name, prev_cmd_txt, varable):
    # Время
    if cmd == 'now_time':
        now = datetime.datetime.now()
        say('Сейчас ' + str(now.hour) + ':' + str(now.minute))
    
    if cmd == 'mind':
        if 'напомни в' in cmd_name or 'будильник на' in cmd_name:
            mind('in_time', prev_cmd_txt)
        
        if 'напомни через' in cmd_name or 'таймер на' in cmd_name:
            mind('plus_time', prev_cmd_txt)
    
    # Работа с браузером
    elif cmd == 'search_google':
        if prev_cmd_txt != '':
            try:
                result = wikipedia.summary(prev_cmd_txt, sentences=5)
                replace_it = {'==': '',
                              '\n\n': '\n',
                              '--': '-',
                              '—': ' - '}
                for i, j in replace_it.items():
                    while i in result:
                        result = result.replace(i, j)
                newres = ''
                start_skob = False
                preds = 0
                for i in result.split(' '):
                    if not start_skob and i != '':
                        if '(' in i:
                            start_skob = True
                        else:
                            newres += ' ' + i
                            if '.' in i:
                                preds += 1
                                if preds > 1 and len(newres.split(' ')) > 15:
                                    break
                    elif ')' in i:
                        start_skob = False
                    
                say('Вот статья из википедии\n' + newres)
                
            except Exception as e:
                print(e)
                webbrowser.get('opera-gx').open(
                    'https://www.google.com/search?client=opera-gx&sourceid=opera&ie=UTF-8&oe=UTF-8&q=' + prev_cmd_txt.replace(
                        ' ', '+'))
                say('Ищу в браузере' + prev_cmd_txt)
    
    elif cmd == 'open_site':
        if prev_cmd_txt != '':
            webbrowser.get('opera-gx').open(prev_cmd_txt)
            say('Захожу на' + prev_cmd_txt)
    
    elif cmd == 'play_music':
        webbrowser.get('opera-gx').open(
            'https://www.youtube.com/watch?v=hTWKbfoikeg&list=PL_eFI2vJpFILfYfjq6xdt92RhRizWk50y&index=1')
        say('Приятного прослушивания!')
    
    elif cmd in ['brs_wk_close', 'brs_wk_return', 'brs_wk_undo', 'brs_wk_redo', 'brs_vid_past', 'brs_vid_next',
                 'brs_vid_stpl', 'brs_vid_full', 'brs_vid_rewind']:
        win32gui.EnumWindows(opera_work, [cmd, prev_cmd_txt])
    
    elif cmd == 'brs_vid_find':
        webbrowser.get('opera-gx').open(
            'https://www.youtube.com/results?search_query=' + prev_cmd_txt.replace(' ', '+'))
        say('Ищу ' + prev_cmd_txt)
    
    # Работа с клавиатурой
    elif cmd == 'kb_write':
        keyboard.write(prev_cmd_txt, 0.01)
        say('Напечатано!')
    
    elif cmd == 'kb_click':
        try:
            keyboard.press(prev_cmd_txt.split()[0])
            say('Есть!')
        except:
            say('Кнопка не нажата')
    
    elif cmd == 'kb_write_long_start':
        say('Печатаю')
        last_text = [prev_cmd_txt + ' ']
        keyboard.write(prev_cmd_txt + ' ', 0.01)
        varable.long_text = True
        varable.last_text = last_text
    
    elif cmd in ['kb_cut', 'kb_copy', 'kb_paste', 'kb_undo', 'kb_redo']:
        h_keys = {'kb_cut': 'ctrl+x', 'kb_copy': 'ctrl+c', 'kb_paste': 'ctrl+v', 'kb_undo': 'ctrl+z',
                  'kb_redo': 'ctrl+shift+z'}
        keyboard.send(h_keys[cmd])
        say('Выполнено')
    
    # Работа с мышью
    elif cmd in ['mb_scroll_up', 'mb_scroll_down']:
        m_keys = {'mb_scroll_up': 9, 'mb_scroll_down': -9}
        mouse.wheel(m_keys[cmd])
    
    # Работа с окнами
    elif cmd in ['kill_process', 'enable_process', 'disable_process', 'foreground_process']:
        t_cmd_text = rus_to_eng(prev_cmd_txt)
        win32gui.EnumWindows(work_process, (t_cmd_text, prev_cmd_txt, cmd))
    
    elif cmd == 'start_process':
        print(prev_cmd_txt, 'asdasd')
        filename = rus_to_eng(prev_cmd_txt)
        if filename != '':
            filepath = 'C:\\VOICE_PROGS\\'
            if filename in [i.split('.')[0] for i in os.listdir(filepath)]:
                os.startfile(filepath + filename)
                say('запускаю ' + prev_cmd_txt)
            else:
                finded = False
                steam_path_name = 'D:\\SteamLibrary\\steamapps\\common\\'
                steam_games = os.listdir(steam_path_name)
                steam_games_lower = [i.lower() for i in steam_games]
                for i in steam_games_lower:
                    if filename in i:
                        game_path = steam_path_name + steam_games[steam_games_lower.index(i)]
                        files_in_game_path = os.listdir(game_path)
                        for j in files_in_game_path:
                            if '.exe' in j:
                                if filename in j:
                                    os.startfile(game_path + '\\' + j)
                                    finded = True
                                    break
                    if finded:
                        break
                
                if not finded:
                    say('приложение не найдено!')
    
    # Работа с заметками
    elif cmd == 'add_note':
        notes = open('notes.txt', 'a', encoding='utf-8')
        notes.write(prev_cmd_txt + '\n\n')
        notes.close()
        say('Выполнено')
    
    elif cmd == 'read_note':
        file = open('notes.txt', 'r', encoding='utf-8')
        notes = file.read()
        file.close()
        all_notes = []
        num_note = 1
        for note in notes.split('\n'):
            if note != '':
                all_notes.append(str(num_note) + ' ' + note)
                num_note += 1
        say(all_notes)
    
    elif cmd == 'delete_note':
        file = open('notes.txt', 'r', encoding='utf-8')
        notes = file.read()
        file.close()
        while '\n\n' in notes:
            notes = notes.replace('\n\n', '\n')
        need_num = to_num(prev_cmd_txt.split()[0])
        new = ''
        notes = notes.split('\n')
        for i in range(len(notes)):
            if i != need_num - 1:
                new += notes[i] + '\n\n'
        file = open('notes.txt', 'w', encoding='utf-8')
        file.write(new)
        file.close()
        say('Выполнено')
    
    # Изменить громкость
    elif cmd.split('_')[-1] == 'volume':
        try:
            vol = 0
            varable.last_volume = get_volume()
            if prev_cmd_txt != '' and prev_cmd_txt.split()[0] == 'максимум':
                vol = 100
            elif cmd.split('_')[0] not in ['once', 'min']:
                vol = to_num(prev_cmd_txt.split()[0])
                
            VOLUME_CHANGE = 4
            comms = {'set_volume': vol,
                     'once_pl_change_volume': varable.last_volume + VOLUME_CHANGE,
                     'once_mi_change_volume': varable.last_volume - VOLUME_CHANGE,
                     'min_volume': 0, }
            set_volume(comms[cmd])
            say(f'громкость установлена на {comms[cmd]}')
            varable.last_volume = comms[cmd]
        except Exception as e:
            print(f'[ERROR] {e}')
            say('неправильное значение')
    
    # Посчитать
    elif cmd == 'calculate':
        
        num = calculate(varable.last_calculated, prev_cmd_txt)
        varable.last_calculated = num
    
    # Приостановить Утёнка
    elif cmd in ['quite_normal', 'quite_angry']:
        if prev_cmd_txt == '':
            outs = {'quite_normal': 'До свидания', 'quite_angry': 'соСи хуй, мудила'}
            say(outs[cmd])
            varable.name_said = False
    
    # Выключение / сон / перегазгрузка
    elif cmd in ['pc_shutdown', 'pc_sleep', 'pc_reboot']:
        now = datetime.datetime.now().hour
        bye_end = ''
        if now < 7:
            bye_end = 'Удачи вам выспаться'
        elif now < 13:
            bye_end = 'Хорошего дня!'
        elif now < 18:
            bye_end = 'Хорошего вечера!'
        else:
            bye_end = 'Спокойной ночи'
        ends = {'pc_shutdown': ['/s /f /t 0', bye_end],
                'pc_sleep': ['/h /t 0', 'До встречи, буду вас ждать'],
                'pc_reboot': ['/r /f /t 0', 'Скоро увидимся']}
        say(ends[cmd][1])
        os.system('shutdown ' + ends[cmd][0])
