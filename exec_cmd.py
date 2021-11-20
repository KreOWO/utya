import os
import datetime
import webbrowser
import win32gui
import keyboard

from opts import to_transcript
from opts import say
from process import work_process
from process import opera_work
from process import set_volume


def exec_cmd(cmd, prev_cmd_txt):
	# Время
	if cmd == 'now_time':
		now = datetime.datetime.now()
		say('Сейчас' + str(now.hour) + ':' + str(now.minute))

	# Работа с браузером
	elif cmd == 'search_google':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open(
				'https://www.google.com/search?client=opera-gx&sourceid=opera&ie=UTF-8&oe=UTF-8&q=' + prev_cmd_txt.replace(
					' ', '+'))
			say('Ищу ' + prev_cmd_txt)

	elif cmd == 'open_site':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open(prev_cmd_txt)
			say('Захожу на' + prev_cmd_txt)

	elif cmd == 'play_music':
		webbrowser.get('opera-gx').open(
			'https://www.youtube.com/watch?v=hTWKbfoikeg&list=PL_eFI2vJpFILfYfjq6xdt92RhRizWk50y&index=1')
		say('Приятного прослушивания!')

	elif cmd in ['brs_wk_close', 'brs_wk_return', 'brs_wk_undo', 'brs_wk_redo', 'brs_vid_past', 'brs_vid_next',
	             'brs_vid_stpl', 'brs_vid_full']:
		win32gui.EnumWindows(opera_work, cmd)
		say('Выполнено')

	# Работа с клавиатурой
	elif cmd == 'kb_write':
		keyboard.write(prev_cmd_txt, 0.05)
		say(prev_cmd_txt + ' напечатано!')

	elif cmd in ['kb_cut', 'kb_copy', 'kb_paste', 'kb_undo', 'kb_redo']:
		h_keys = {'kb_cut': 'ctrl+x', 'kb_copy': 'ctrl+c', 'kb_paste': 'ctrl+v', 'kb_undo': 'ctrl+z',
		          'kb_redo': 'ctrl+shift+z'}
		keyboard.send(h_keys[cmd])
		say('выполнено')

	# Работа с окнами
	elif cmd in ['kill_process', 'enable_process', 'disable_process']:
		win32gui.EnumWindows(work_process, (prev_cmd_txt, cmd))

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
			if prev_cmd_txt == 'ноль':
				prev_cmd_txt = '0'
			vol = int(prev_cmd_txt)
			set_volume(vol)
			say('громкость установлена на' + prev_cmd_txt)
		except:
			say('неправильное значение')

	# Приостановить Утёнка
	elif cmd in ['quite_normal', 'quite_angry']:
		outs = {'quite_normal': 'До свидания', 'quite_angry': 'соСи хуй, мудила'}
		say(outs[cmd])
		return 'name_sayed', False

	# Выключение / сон / перегазгрузка
	elif cmd in ['pc_shutdown', 'pc_sleep', 'pc_reboot']:
		ends = {'pc_shutdown': ['/s /f /t 0', 'Спокойной ночи'], 'pc_sleep': ['/h /t 0', 'До встречи, буду вас ждать'],
		        'pc_reboot': ['/r /f /t 0', 'Скоро увидимся']}
		say(ends[cmd][1])
		os.system('shutdown ' + ends[cmd][0])
