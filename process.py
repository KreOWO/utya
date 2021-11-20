import win32gui
import win32con
import keyboard
import ctypes

from opts import to_transcript
from opts import say


def work_process(hwnd, extra):
    prev_cmd_txt, flag = extra
    t_cmd_text = to_transcript(prev_cmd_txt)
    process_name = win32gui.GetWindowText(hwnd)
    if process_name != '' and prev_cmd_txt != '':
        if prev_cmd_txt in process_name.lower() or t_cmd_text in process_name.lower():
            if flag == 'kill_process':
                try:
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE)
                    say(prev_cmd_txt + ' закрыто')
                except:
                    say('отказано в доступе')

            if flag == 'enable_process':
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                say(prev_cmd_txt + ' развёрнуто')

            if flag == 'disable_process':
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
                say(prev_cmd_txt + ' свёрнуто')


def opera_work(hwnd, extra):
    flag = extra
    process_name = win32gui.GetWindowText(hwnd)
    if 'opera' in process_name.lower():
        was = win32gui.IsIconic(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        sends = {'brs_wk_close':'ctrl+w', 'brs_wk_return': 'ctrl+shift+t', 'brs_wk_undo': 'ctrl+left', 'brs_wk_redo':'ctrl+right',
                 'brs_vid_past': 'shift+p', 'brs_vid_next': 'shift+n', 'brs_vid_stpl':'k', 'brs_vid_full': 'f'}
        keyboard.send(sends[flag])
        if was:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


def vol_change_once(btn):
    if btn == 'down':
        btn = 0xAE
    else:
        btn = 0xAF
    for j in [0, 0x0002]:
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(btn, 0x48, j, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def set_volume(volume):
    for i in range(0, 50):
        vol_change_once('down')

    for i in range(volume // 2):
        vol_change_once('up')


class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]


class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]


class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]


class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]
