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

		was = win32gui.IsIconic(hwnd);
		win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
		sends = {'brs_wk_close':'ctrl+w', 'brs_wk_return': 'ctrl+shift+t', 'brs_wk_undo': 'ctrl+left', 'brs_wk_redo':'ctrl+right',
				 'brs_vid_past': 'shift+p', 'brs_vid_next': 'shift+n', 'brs_vid_stpl':'k', 'brs_vid_full': 'f'}
		keyboard.send(sends[flag])
		print(was)
		if was:
			win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
