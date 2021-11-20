import pyttsx3

t_cript = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')]

opts = {
		'alias': ('у тебя', 'утёнок', 'утя'),
		'tbr': ['сейчас'],
		'cmds': {
			# Время
			'now_time': ['время', 'сколько времени', 'который час', 'что по времени'],
			# Работа с браузером
			'search_google': ['загугли', 'что такое', 'найди'],
			'open_site': ['зайди на'],
			'play_music': ['включи музыку'],  # Будет улучшено
			'brs_wk_close': ['закрой вкладку', 'закрыть вкладку'],
			'brs_wk_return': ['верни вкладку', 'вернуть вкладку', 'сверни вкладку', 'свернуть вкладку'],
			'brs_wk_undo': ['предыдущая вкладка', 'предыдущая страница'],
			'brs_wk_redo': ['следующая вкладка', 'следующая страница'],
				# Работа с видео
				'brs_vid_past': ['предыдущee видео'],
				'brs_vid_next': ['следующее видео'],
				'brs_vid_stpl': ['поставь на паузу', 'продолжи видео', 'останови видео', 'пауза видео'],
				'brs_vid_full': ['fullscreen', 'полный экран'],
			# Работа с клавиатурой
			'kb_write': ['напечатай', 'напечатать'],
			'kb_cut': ['вырежи', 'вырезать'],
			'kb_copy': ['копируй', 'копировать'],
			'kb_paste': ['вставь', 'вставить'],
			'kb_undo': ['назад'],
			'kb_redo': ['вперёд'],
			# Работа с окнами
			'kill_process': ['закрой приложение', 'выйди из', 'закрыть приложение'],
			'enable_process': ['разверни', 'развернуть'],
			'disable_process': ['сверни', 'свернуть'],
			'start_process': ['запустить', 'запусти', 'открой', 'зайди в', 'го в'],
			# будильник / таймер / напоминание
			'mind': ['напомни через', 'поставь будильник на'],  # Будет улучшено
			# Изменить громкость
			'set_volume': ['громкость на', 'звук на'],  # Будет улучшено
			# Посчитать
			'calculate': ['посчитай'],  #
			# Приостановить Утёнка
			'quite_normal': ['пока', 'до встречи', 'бывай', 'спасибо'],
			'quite_angry': ['пошел н****', 'иди в п****'],
			# Выключение / сон / перезагрузка
			'pc_shutdown': ['пуск завершение работы', 'выключи компьютер'],
			'pc_sleep': ['пуск сон', 'переведи в режим сна'],
			'pc_reboot': ['пуск перезагрузка', 'перезагрузи компьютер']
			}}


def say(txt):
	engine = pyttsx3.init()
	engine.say(txt)
	engine.runAndWait()


def to_transcript(txt):
	for i in range(len(t_cript[0])):
		txt = txt.replace(t_cript[0][i], t_cript[1][i])
	return txt
