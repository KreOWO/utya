import os
import datetime
import webbrowser
import win32gui
import keyboard

from opts import say
from process import work_process
from process import opera_work
from process import set_volume
from process import mind
from process import calculate


def exec_cmd(cmd, cmd_name, prev_cmd_txt):
	# Время
	if cmd == 'now_time':
		now = datetime.datetime.now()
		say('Сейчас' + str(now.hour) + ':' + str(now.minute))

	if cmd == 'mind':
		if 'напомни в' in cmd_name or 'будильник на' in cmd_name:
			mind('in_time', prev_cmd_txt)

		if 'напомни через' in cmd_name or 'таймер на' in cmd_name:
			mind('plus_time', prev_cmd_txt)


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

	elif cmd == 'brs_vid_find':
		webbrowser.get('opera-gx').open(
			'https://www.youtube.com/results?search_query=' + prev_cmd_txt.replace(' ', '+'))
		say('Ищу ' + prev_cmd_txt)

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
		prev_cmd_txt = prev_cmd_txt.replace('апекс', 'apex')
		t_cript = [list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя '),
		           'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia| '.split('|')]

		filename = ''.join(
			[int(i in t_cript[0]) * t_cript[1][t_cript[0].index(i)] + int(i in t_cript[1]) * i for i in prev_cmd_txt])

		if filename != '':
			filepath = 'C:\\VOICE_PROGS\\'
			if filename in [i.split('.')[0] for i in os.listdir(filepath)]:
				os.startfile(filepath + filename)
				say('запускаю' + prev_cmd_txt)
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

	# Изменить громкость
	elif cmd == 'set_volume':
		try:
			word_num = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
			if prev_cmd_txt in word_num:
				prev_cmd_txt = prev_cmd_txt.replace(prev_cmd_txt, str(word_num.index(prev_cmd_txt)))
			vol = int(prev_cmd_txt.split(':')[0])
			set_volume(vol)
			say(f'громкость установлена на {vol}')
		except Exception as e:
			print(f'[ERROR] {e}')
			say('неправильное значение')

	# Посчитать
	elif cmd == 'calculate':
		calculate(prev_cmd_txt)


	# Приостановить Утёнка
	elif cmd in ['quite_normal', 'quite_angry']:
		outs = {'quite_normal': 'До свидания', 'quite_angry': 'соСи хуй, мудила'}
		say(outs[cmd])
		return 'name_said', False

	# Выключение / сон / перегазгрузка
	elif cmd in ['pc_shutdown', 'pc_sleep', 'pc_reboot']:
		ends = {'pc_shutdown': ['/s /f /t 0', 'Спокойной ночи'], 'pc_sleep': ['/h /t 0', 'До встречи, буду вас ждать'],
		        'pc_reboot': ['/r /f /t 0', 'Скоро увидимся']}
		say(ends[cmd][1])
		os.system('shutdown ' + ends[cmd][0])
