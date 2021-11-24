from exec_cmd import exec_cmd
from opts import say
from opts import opts

name_said = False

def callback(voice, name_said):
	if not name_said:
		for i in opts['alias']:
			if i in voice:
				say('Слушаю вас')
				name_said = True
	else:
		cmd = voice

		for i in opts['tbr']:
			cmd.replace(i, '')

		new_cmd = []
		for i, j in opts['cmds'].items():
			for g in j:
				if g in cmd and g != '':
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

	return name_said
