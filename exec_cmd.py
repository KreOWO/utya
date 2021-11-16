import os
import datetime
import webbrowser
import win32gui
from sound import Sound

from to_transcript import to_transcript
from say import say
from kill_process import kill_process

def exec_cmd(cmd, name_sayed, prev_cmd_txt):
	if cmd == 'now_time':
		now = datetime.datetime.now()
		say('Сейчас ' + str(now.hour) + ':' + str(now.minute))
		
	elif cmd == 'search_google':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open('https://www.google.com/search?client=opera-gx&sourceid=opera&ie=UTF-8&oe=UTF-8&q=' + prev_cmd_txt.replace(' ', '+'))
			say('Ищу ' + prev_cmd_txt)

	elif cmd == 'open_site':
		if prev_cmd_txt != '':
			webbrowser.get('opera-gx').open(prev_cmd_txt)
			say('Захожу на ' + prev_cmd_txt)

	elif cmd == 'play_music':
		webbrowser.get('opera-gx').open('https://www.youtube.com/watch?v=hTWKbfoikeg&list=PL_eFI2vJpFILfYfjq6xdt92RhRizWk50y&index=1')
		say('Приятного прослушивания!')

	elif cmd == 'write_keys':
		keyboard.write(prev_cmd_txt, 0.05)
		say(prev_cmd_txt + ' напечатано!')
		
	elif cmd == 'kill_process':
			win32gui.EnumWindows(kill_process, (prev_cmd_txt))
		
	elif cmd == 'start_process':
		filename = 'C:\\VOICE_PROGS\\' + to_transcript(prev_cmd_txt)
		try:
			os.startfile(filename)
			say('приложение' + prev_cmd_txt + ' запущено!')
		except:
			say('приложение не найдено!')

	elif cmd == 'set_volume':
		#try:
			vol = int(prev_cmd_txt)
			Sound.volume_set(vol)
			say('громкость установлена на ' + prev_cmd_txt)
		#except:
			say('неправильное значение')

	elif cmd == 'quite_normal':
		say('До свидания')
		return('name_sayed', name_sayed)

	elif cmd == 'quite_angry':
		say('соСи хуй, мудила')
		return('name_sayed', name_sayed)

	elif cmd == 'pc_shutdown':
		say('Спокойной ночи')
		os.system('shutdown /p /f')

	elif cmd == 'pc_sleep':
		say('До встречи, буду вас ждать')
		os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")