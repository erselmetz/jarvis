import talk
import wikipedia
import webbrowser
import pywhatkit
import os
import sys
import reply
import mic
import path

def execute():
    command = mic.take_command()
    # play on youtube
    if 'play' in command:
        text = command.replace('play','')
        talk.say("playing "+text)
        pywhatkit.playonyt(text)
        
    # time
    elif 'check the time' in command:
        print(reply.list['time'])
        talk.say('current time is '+reply.list['time'])

    # wikipedia
    elif 'who is' in command or 'do you know about' in command:
        search = command.replace('who is','')
        search = command.replace('do you know about','')
        result = wikipedia.summary(search, sentences=2)
        print(command)
        talk.say(result)

    # search in browser
    elif 'open' in command or 'launch' in command:
        web = command.replace('open','')
        web = command.replace('open my','')
        web = command.replace('launch','')
        web = command.replace('launch my','')
        talk.say(reply.openning_apps(web))
        webbrowser.open('https://'+web+'.com')

    # open vs code application
    elif 'open vs code' in command:
        talk.say(reply.openning_apps['visual_studio'])
        os.startfile(path.vs_code)

    # exit or close jarvis
    elif 'exit' in command:
        talk.say('closing jarvis')
        sys.exit()

    # find in dictionary
    # elif command in reply.conversation:
    #     talk.say(reply.conversation[command])


# while True:
#     talk.say(reply.list['greet'])
#     execute()

# execute()