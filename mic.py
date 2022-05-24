import speech_recognition as sr

r = sr.Recognizer()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = r.listen(source) 
            command = r.recognize_google(voice)
            command = command.lower()
            print('you say '+command)
    except:
        pass
    return command
