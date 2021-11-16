t_cript = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')]

def to_transcript(txt):
	for i in range(len(t_cript[0])):
		txt = txt.replace(t_cript[0][i], t_cript[1][i])
	return txt