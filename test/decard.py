import requests
from bs4 import BeautifulSoup
import time
from telepot.loop import MessageLoop
from pprint import *
import random

bot = telepot.Bot('664350005:AAEGmjiy3KutiBEqPsfvf-JQsFSquDxa_To')
dcarddic={"熱門":"","新生季":"/freshman"
,"美妝":"/mackup","感情":"/relationship"
,"心情":"/mood","女孩":"/girl","有趣":"/funny"
,"攝影":"/photography","3C":"/3c","西斯":"/sex"
,"廢文":"/whysoserious","課程":"/course"
,"工作":"/job","理財":"/money","男孩":"/boy"
,"運動":"/sport","實習職缺":"/intern"}
url=[]
def TooLong(x):
    count=0
    for y in x:
        if count>=30:
            count=0
            print(y)
        else:
            print(y,end="")
            count=count+1
print("你的選擇有 : ")  


dcardurl="http://www.dcard.tw/f"
wheresearch=dcarddic[input("\n你想爬哪一個版的資料呢? :")]
print(wheresearch)
r=requests.get(dcardurl+wheresearch, timeout = 5)    
print(r.url)
soup=BeautifulSoup(r.text, 'html.parser')

a_tags = soup.find_all("div",class_="PostList_entry_1rq5L PostList_cozy_39tW6")

inpu=int(input("你要找幾筆資料:"))+2
time=0
for x in range(inpu):
    href_a=a_tags[x].find("a",class_="PostEntry_root_V6g0r")
    header=a_tags[x].find("span",class_="PostEntry_pinned_2AouY")
    try :
        if str(header.string)=="置頂":
            pass
    except:
        url.append("http://www.dcard.tw"+href_a.get('href'))
        time=time+1
    finally:
        if time==3:
            break
        
cline="*"*75
for x in url:
    tmp=requests.get(x,timeout=5)
    x_soup=BeautifulSoup(tmp.text,'html.parser')
    text=x_soup.find("div",class_="Post_content_NKEl9")
    title=x_soup.find("h2",class_="Post_title_2O-1e")
    ntext=text.get_text().split(" ")
    print("標題",title.get_text(),"\n\n")
    for y in ntext:    
        TooLong(y)
        print()
    print(x,"\n",cline)
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
    if flag == 'Mao_secretary_bot' and First_command=='/start':
        bot.sendMessage(chat_id, "輸入你想搜尋的板\n你的選擇有 : \n熱門,新生季,美妝,感情,心情,女孩,有趣,攝影,3C,西斯,廢文,課程,工作,理財,男孩,運動,實習職缺")
    elif flag == 'Mao_secretary_bot' and First_command in dcarddic:
    else:
        pass
    
   
    
MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while True:
    time.sleep(5)