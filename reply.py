import random
import datetime

def openning_apps(params):
    a = [
        'opening '+params,
        'ok i will now open '+params,
        'please wait a minute',
        params+' is now loading'
    ]
    return random.choice(a)

list = {
    'greet': random.choice(['hello master','hi master']),
    'time': datetime.datetime.now().strftime('%I:%M %p')
}

conversation = {
    'how are you': random.choice(['I am fine','I`m ok','I am ok','i feel bless','not bad']),
    'what is your favorate color': random.choice(['my favorate color is green','green','well it`s color green']),
    'do you have a boyfriend': random.choice(['no i dont have','i dont have a time for that']),
    'do you have a girlfriend': random.choice(['no i dont have','i dont have a time for that']),
}