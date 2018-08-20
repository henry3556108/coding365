import telepot
import time
from telepot.loop import MessageLoop
from pprint import *
import random

bot = telepot.Bot('664350005:AAEGmjiy3KutiBEqPsfvf-JQsFSquDxa_To')
#print(bot.getMe())
state=None
game=None
class Dice:
    def __init__(self):
        self.time=0
        self.temp=[]
        self.playerdic={}
        self.player=[]
        self.now=''
        self.dice=[]
    def InitData(self):
        print("Data init")
        datatemp=[]
        time=0
        for x in self.player:
            self.playerdic[x+str(time)]=[]
            for _ in range(6):
                self.playerdic[x+str(time)].append(str(random.randint(1,6)))
            print(self.playerdic[x+str(time)])
            time=time+1
        self.now=self.player[0]
    def Scanner(self,commend,user):
        if len(commend)==1 and commend[0]=="抓" and user!=self.now:
            print("抓")
            return True
        if len(commend)==2 and commend[0].isdigit()==True and commend[1].isdigit()==True and user==self.now:
            print("喊")
            if len(self.dice)==0 and int(commend[0])>0 and int(commend[1])>0:
                print("1")
                return True
            elif int(self.dice[0])<int(commend[0]) and int(self.dice[1])<=int(commend[1]) :
                print("2")
                return True
            elif int(self.dice[0])<=int(commend[0]) and int(self.dice[1])<int(commend[1]):
                print("2")
                return True
            else:
                return False
        else:
            return False
    def Playing(self,commend,user):
        self.dice=[commend[0],commend[1]]
        print(self.playerdic)
        print(self.dice)
        self.time=self.time+1
        if self.time==len(self.player):
            self.time=0
    def WhoWin(self,commend,user):
        print("good")

def PlayingState(game,command,user):
    print("3")
    if len(command)==2:
        game.now=game.player[game.time]
        game.Playing(command,user)
    if command[0]=='抓':
        print("5")
        game.WhoWin(command,user)

def Command(name,command):
    global state,game
    if command=='/join'and state=='join':
        game.player.append(name)
        bot.sendMessage(chat_id, 'join')
    elif command=='/吹牛' and state==None:
        game=Dice()
        state='join'
        bot.sendMessage(chat_id, "吹牛遊戲開始\n玩家開始加入")
    elif command=='/start' and state=='join':
        state='start'
        game.InitData()

def handle(msg):
    pprint(msg)
    try:  
        global chat_id
        chat_id= msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        First_command = msg['text'].split('@')[0]
        First_command = First_command
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        pass
    if flag == 'Mao_secretary_bot':
        Command(username,First_command)
    else:
        pass
    First_command=First_command.split(",")
    if state=='start' and game.Scanner(First_command,username)==True and flag == 'Mao_secretary_bot': 
        PlayingState(game,First_command,username)
   
    
MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while True:
    time.sleep(5)