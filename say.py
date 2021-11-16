import pyttsx3

def say(txt):
	engine = pyttsx3.init()
	engine.say(txt)
	engine.runAndWait()