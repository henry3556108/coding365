import requests
from bs4 import BeautifulSoup
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
            
data={"source":"hp","q": "Youtube","oq":"Youtube"}
r=requests.get("http://www.dcard.tw/f", timeout = 5)    

soup=BeautifulSoup(r.text, 'html.parser')

a_tags = soup.find_all("div",class_="PostList_entry_1rq5L PostList_cozy_39tW6")

inpu=int(input("你要找幾筆資料:"))

for x in range(inpu):
    href_a=a_tags[x].find("a",class_="PostEntry_root_V6g0r")
    url.append("http://www.dcard.tw"+href_a.get('href'))
cline="*"*50
for x in url:
    tmp=requests.get(x,timeout=5)
    x_soup=BeautifulSoup(tmp.text,'html.parser')
    text=x_soup.find("div",class_="Post_content_NKEl9")
    #print(text)
    ntext=text.get_text().split(" ")
    for y in ntext:    
        TooLong(y)
        print()
    print(x,"\n",cline)
