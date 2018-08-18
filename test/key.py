import telepot
import time
from telepot.loop import MessageLoop
from pprint import *
bot = telepot.Bot('664350005:AAEGmjiy3KutiBEqPsfvf-JQsFSquDxa_To')
#print(bot.getMe())
player=[]
state=None
class Dice:
    def __init__(self):
        temp=[]
    def InitData(self):
        print("InitData")
    def Scanner(self):
        return True
    def Playing(self):
        print("Playing")
    def WhoWin(self):
        print("WhoWin")

def PlayingState(game):
    print("i'm here",type(game))
    game.InitData()
    bot.sendMessage(chat_id, '遊戲正式開始')
    game.Scanner()
    game.Playing()
    game.WhoWin()

def Command(name,command):
    global state
    if command=='/join'and state=='join':
        global player
        player.append(name)
        bot.sendMessage(chat_id, 'join')
    elif command=='/吹牛' and state==None:
        global game
        game=Dice()
        state='join'
        bot.sendMessage(chat_id, "吹牛遊戲開始\n玩家開始加入")
def handle(msg):
    pprint(msg)
    try:  
        global chat_id
        chat_id= msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        First_command = msg['text'].split('@')[0]
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        pass
    if flag == 'Mao_secretary_bot':
        Command(username,First_command)
    else:
        pass
    #bot.sendMessage(chat_id, First_command)
    global state,player
    if state=='start' and game.Scanner()==True:    
        PlayingState(game)
    if First_command=='/start' and state=='join':
        state='start'
    
MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while True:
    time.sleep(5)