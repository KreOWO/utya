import win32gui

from to_transcript import to_transcript
from say import say

def kill_process(hwnd, extra):
	killed = False
	prev_cmd_txt = extra
	t_cmd_text = to_transcript(prev_cmd_txt)
	process_name = win32gui.GetWindowText(hwnd)
	rect = win32gui.GetWindowRect(hwnd)
	if process_name != '' and prev_cmd_txt != '':
		print(process_name)
		if prev_cmd_txt in process_name.lower() or t_cmd_text in process_name.lower():
			print(process_name)
			try:
				win32gui.PostMessage(hwnd, 0x0010);
				say('приложение' + prev_cmd_txt + ' закрыто')
			except:
				say('отказано в доступе')