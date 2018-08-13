from selenium import webdriver
from time import *

Taiwan_Dic={'基隆':"KeelungList",'台北市':'TaipeiCityList','新北市':'TaipeiList'}
inpu=input("input:")
city=Taiwan_Dic[inpu]
x=webdriver.Firefox()
x.get("https://www.cwb.gov.tw/V7/forecast/")

tmp = x.find_element_by_id(city)
print("現在 {} 溫度為 {} 濕度為 {} 天氣狀況為 {}".format(city,tmp.find_elements_by_tag_name('td')[1].text,tmp.find_elements_by_tag_name('td')[2].text,tmp.find_element_by_css_selector("img").get_attribute("title")))

sleep(3)

x.quit()