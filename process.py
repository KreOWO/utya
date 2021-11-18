import win32gui
import win32con
import win32api
import time
import keyboard

from opts import to_transcript
from opts import say

def work_process(hwnd, extra):
	killed = False
	prev_cmd_txt, flag = extra
	t_cmd_text = to_transcript(prev_cmd_txt)
	process_name = win32gui.GetWindowText(hwnd)
	if process_name != '' and prev_cmd_txt != '':
		if prev_cmd_txt in process_name.lower() or t_cmd_text in process_name.lower():
			if flag == 'kill_process':
				try:
					win32gui.PostMessage(hwnd, win32con.WM_CLOSE);
					say(prev_cmd_txt + ' закрыто')
				except:
					say('отказано в доступе')

			if flag == 'enable_process':
				win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
				say(prev_cmd_txt + ' развёрнуто')

			if flag == 'disable_process':
				win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
				say(prev_cmd_txt + ' свёрнуто')


def klose_vklad(hwnd, extra):
	flag = extra
	process_name = win32gui.GetWindowText(hwnd)
	if 'opera' in process_name.lower():
		win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, 1, 0)
		sends = {'brs_vk_close':'ctrl+w', 'brs_vk_return': 'ctrl+shift+t', 'brs_vk_undo': 'ctrl+left', 'brs_vk_redo':'ctrl+right'}
		keyboard.send(sends[flag])