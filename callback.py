from exec_cmd import exec_cmd
from asyncs import say
from opts import opts
import re

def callback(voice, name_said, long_text):
	if not name_said:
		for i in ('у тебя', 'утёнок', 'утя', 'утенок'):
			if i in voice:
				say('Слушаю вас')
				name_said = True
	else:
		if long_text:
			if 'перестань печатать' in voice or 'конец текста' in voice:
				say('Закончил')
				long_text = False
			else:
				exec_cmd('kb_write', '', voice + ' ')
		else:
			cmd = voice
			new_cmd = []
			for i, j in opts.items():
				for g in j:
					if g != '' and g in cmd:
						new_cmd.append([i, g])

			if len(new_cmd) > 0:
				cmd = [new_cmd[0][1] + cmd.split(new_cmd[0][1])[1]]

				for i in new_cmd:
					cmd[-1] = cmd[-1].split(i[1])
					cmd[-1][1] = i[1] + cmd[-1][1]
					last_cmd = []
					for j in cmd[-1]:
						last_cmd.append(j)
					cmd = cmd[:-1]
					for j in last_cmd:
						cmd.append(j)

				for i in range(len(cmd) - 1):
					flag_ch = exec_cmd(*new_cmd[i], cmd[i + 1].replace(new_cmd[i][1], '').strip())
					if flag_ch is not None:
						if flag_ch[0] == 'name_said':
							name_said = flag_ch[1]
						if flag_ch[0] == 'long_text':
							long_text = True

	return name_said, long_text
