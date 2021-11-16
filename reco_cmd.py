from fuzzywuzzy import fuzz
from opts import opts

def reco_cmd(cmd):
	RC = {
		  'cmd': '',
		  'percent': 0
		  }
	for i, j in opts['cmds'].items():
		for g in j:
			if g in cmd:
				cmd = cmd[cmd.find(g):]
			vrt = fuzz.ratio(cmd, g)
			if vrt > RC['percent']:
				RC['cmd'] = i
				RC['percent'] = vrt

	return RC