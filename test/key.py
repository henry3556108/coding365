import telepot
import time
from telepot.loop import MessageLoop
from pprint import *
import random

test=(
"吹牛遊戲開始\n"
"玩家開始加入\n"
"/join@Mao_secretary_bot---加入\n"
"/start@Mao_secretary_bot---開始遊戲\n"
"數字,數字@Mao_secretary_bot---吹牛\n"
"抓@Mao_secretary_bot---抓"
)
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
            self.playerdic[x]=[]
            for _ in range(6):
                self.playerdic[x].append(str(random.randint(1,6)))
            self.playerdic[x].sort()
            print(self.playerdic[x],x)
        self.now=self.player[time]
    def Scanner(self,commend,user):
        print(len(commend),commend[0],user,self.now)
        if len(commend)==1 and commend[0]=="抓" and user==self.now:
            return True
        if len(commend)==2 and commend[0].isdigit()==True and commend[1].isdigit()==True and user==self.now:
            if len(self.dice)==0 and int(commend[0])>0 and int(commend[1])>0:
                return True
            elif int(self.dice[0])<int(commend[0]) and int(self.dice[1])<=int(commend[1]) :
                return True
            elif int(self.dice[0])<=int(commend[0]) and int(self.dice[1])<int(commend[1]):
                return True
            else:
                return False
        else:
            return False
    def Playing(self,commend,user):
        self.dice=[commend[0],commend[1]]
        self.time=self.time+1
        if self.time==len(self.player):
            self.time=0
    def WhoWin(self,commend,user):
        playerdice=self.playerdic[self.now]
        tempquant=self.dice[0]
        tempnum=self.dice[1]
        if playerdice.count(tempnum)+playerdice.count("1")>=int(tempquant):
            bot.sendMessage(chat_id, "你抓錯了 你是笨海豹 他的骰子有:")
            bot.sendMessage(chat_id, game.playerdic[game.now])
        else:
            bot.sendMessage(chat_id, "你抓對了 你是有腦袋海豹 他的骰子有:")
            bot.sendMessage(chat_id, game.playerdic[game.now])
        global state
        state="over"


def PlayingState(game,command,user):
    if len(command)==2:
        print(game.time)
        game.now=game.player[game.time]
        game.Playing(command,user)
        game.time=game.time+1
        if game.time==len(game.player):
            game.time=0
    if command[0]=='抓':
        game.WhoWin(command,user)
    global state,chat_id
    if state!="over":
        bot.sendMessage(chat_id, game.dice)

def Command(name,command):
    global state,game
    if command=='/join'and state=='join':
        game.player.append(name)
        bot.sendMessage(chat_id, 'join')
    elif command=='/吹牛' and state==None:
        game=Dice()
        state='join'
        bot.sendMessage(chat_id, test)
    elif command=='/start' and state=='join':
        state='start'
        bot.sendMessage(chat_id, "遊戲開始")
        game.InitData()
    elif state=="over":
        game=None
        state=None
        bot.sendMessage(chat_id, "遊戲結束")

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
    First_command=First_command.split(",")
    if state=='start' and game.Scanner(First_command,username)==True and flag == 'Mao_secretary_bot':
        PlayingState(game,First_command,username)
        Command(username,First_command)
    
MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while True:
    time.sleep(5)