import speech_recognition as sr

from exec_cmd import exec_cmd
from opts import say
from opts import opts

def callback(voice, name_sayed):
	for i in opts['alias']:
		if i in voice:
			voice = voice[voice.find(i):]

	if not name_sayed:
		if voice.startswith(opts['alias']):
			say('Слушаю вас')
			name_sayed = True

	else:
		cmd = voice

		for i in opts['tbr']:
			cmd.replace(i, '')

		new_cmd = ['', '']
		for i, j in opts['cmds'].items():
			for g in j:
				if g in cmd and g != '':
					new_cmd = [i, g]

		print(new_cmd)
		prev_cmd_txt = cmd[cmd.find(new_cmd[1]) + len(new_cmd[1]) + 1:]
		flag_ch = exec_cmd(new_cmd[0], name_sayed, prev_cmd_txt)
		if flag_ch != None:
			if flag_ch[0] == 'name_sayed': name_sayed = flag_ch[1]

	return name_sayed