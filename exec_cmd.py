import os
import datetime
import webbrowser
import win32gui
import keyboard
from imports.sound import Sound

from to_transcript import to_transcript
from say import say
from kill_process import kill_process

def exec_cmd(cmd, name_sayed, prev_cmd_txt):
	# Время
	if cmd == 'now_time':
		now = datetime.datetime.now()
		say('Сейчас' + str(now.hour) + ':' + str(now.minute))

	# Работа с браузером
	elif cmd == 'search_google':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open('https://www.google.com/search?client=opera-gx&sourceid=opera&ie=UTF-8&oe=UTF-8&q=' + prev_cmd_txt.replace(' ', '+'))
			say('Ищу ' + prev_cmd_txt)

	elif cmd == 'open_site':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open(prev_cmd_txt)
			say('Захожу на' + prev_cmd_txt)

	elif cmd == 'play_music':
		webbrowser.get('opera-gx').open('https://www.youtube.com/watch?v=hTWKbfoikeg&list=PL_eFI2vJpFILfYfjq6xdt92RhRizWk50y&index=1')
		say('Приятного прослушивания!')
		
	# Работа с клавиатурой
	elif cmd == 'kb_write':
		keyboard.write(prev_cmd_txt, 0.05)
		say(prev_cmd_txt + ' напечатано!')
		
	elif cmd == 'kb_cut':
		keyboard.send('ctrl+x')
		say('вырезано')
		
	elif cmd == 'kb_copy':
		keyboard.send('ctrl+c')
		say('копировано')
		
	elif cmd == 'kb_paste':
		keyboard.send('ctrl+v')
		say('вставлено')
		
	elif cmd == 'kb_hotkey':
		prev_cmd_txt = to_transcript(prev_cmd_txt)
		prev_cmd_txt = prev_cmd_txt.replace('kontrol', 'ctrl')
		prev_cmd_txt = prev_cmd_txt.replace('kontrl', 'ctrl')
		prev_cmd_txt = prev_cmd_txt.replace('control', 'ctrl')
		print(prev_cmd_txt)
		keyboard.send(prev_cmd_txt.replace(' ', '+'))
		
	# Работа с окнами
	elif cmd == 'kill_process':
			win32gui.EnumWindows(kill_process, (prev_cmd_txt))
		
	elif cmd == 'start_process':
		filename = 'C:\\VOICE_PROGS\\' + to_transcript(prev_cmd_txt)
		try:
			os.startfile(filename)
			say('запускаю приложение' + prev_cmd_txt)
		except:
			say('приложение не найдено!')
			
	# Изменить громкость
	elif cmd == 'set_volume':
		try:
			if prev_cmd_txt == 'ноль': prev_cmd_txt = '0'
			vol = int(prev_cmd_txt)
			Sound.volume_set(vol)
			say('громкость установлена на' + prev_cmd_txt)
		except:
			say('неправильное значение')

	# Приостановить Утёнка
	elif cmd == 'quite_normal':
		say('До свидания')
		return('name_sayed', False)

	elif cmd == 'quite_angry':
		say('соСи хуй, мудила')
		return('name_sayed', False)

	# Выключение / сон / перегазгрузка
	elif cmd == 'pc_shutdown':
		say('Спокойной ночи')
		os.system('shutdown /s /f /t 0')

	elif cmd == 'pc_sleep':
		say('До встречи, буду вас ждать')
		os.system('shutdown /h /t 0')

	elif cmd == 'pc_reboot':
		say('Скоро увидимся')
		os.system('shutdown /r /f /t 0')