from exec_cmd import exec_cmd
from asyncs import say
from opts import opts


def callback(voice, name_said, long_text, last_text):
	if not name_said:
		if voice in ['у тебя', 'утёнок', 'утя', 'утенок']:
			say('Слушаю вас')
			name_said = True
	else:
		if long_text:
			if voice in ['конец текста', 'перестань печатать']:
				last_text = []
				say('Закончил')
				long_text = False
			elif voice in ['отмена', 'вернуть', 'назад'] and last_text != []:
				exec_cmd('kb_write', '', len(last_text[-1]) * '\b')
				last_text = last_text[:-1]
			else:
				last_text.append(voice + ' ')
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
							last_text = flag_ch[1]

	return name_said, long_text, last_text

#