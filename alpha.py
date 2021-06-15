import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
alpha = pyttsx3.init()
while True:
 with sr.Microphone() as source:
    print("say somthing.....")
    voice = listener.listen(source)
    identify = listener.recognize_google(voice)
    word = identify
    if "who are you" in word and "alpha" not in word:
       alpha.say("i am alpha; version 1.0. I AM A VOICE REPEATOR; created by AMJAD ; AND HIS AASHAAN. RIJFAAS. your good name please")
       alpha.runAndWait()
       voice = listener.listen(source)
       identify = listener.recognize_google(voice)
       word = identify
       alpha.say(f'''hello{word}''')
       alpha.runAndWait()
    elif "ALPHA" in word:
       alpha.say(word)
       alpha.runAndWait()
    else:
       alpha.say("hi, i am ALPHA; if you want to speak with me; say. HEY, ALPHA")
       alpha.runAndWait()


       pass



