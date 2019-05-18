
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import string
import sys

from datetime import datetime

cinemalist = ['강남','강변','건대입구','구로','대학로','동대문','등촌','명동','명동역 씨네라이브러리','목동','미아','불광','상봉','성신여대입구','송파','수유','신촌아트레온','씨네드쉐프 압구정','씨네드쉐프 용산','압구정','여의도','영등포','왕십리','용산아이파크몰','중계','천호','청담씨네시티','피카디리1958','하계','홍대']
indexnum = 0
# 클라이언트에서 실행 인자로 date(ex:20190515), cinema(ex:CGV강남"), movie(ex:명탐정 피카츄), movietime(ex:21:05)
# 위 처럼 실행 인자가 총 4개 필요합니다. date cinema movie movietime
# 임의로 date cinema movie movietime을 설정해서 실행하는 코드로 짰습니다.

#date = "20190518"
#cinema = "왕십리"
#movie = "걸캅스"
#movietime = "24:00"

date = sys.argv[1]
cinema = sys.argv[2]
movie = sys.argv[3]
movietime = sys.argv[4]


for indexnum in range(0,30):
    
    if cinemalist[indexnum]==cinema:
        indexnum=indexnum+1
        break

driver=webdriver.Chrome('/Users/songsari/Desktop/chromedriver')

# https://sites.google.com/a/chromium.org/chromedriver/downloads 에서 설치
driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/Schedule/?tc=0001&t=T&ymd='+date+'&src=')

driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()

driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li['+str(indexnum)+']/a').click()

time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

movielist = soup.select('#divContent > section > h3')
ite = 0
for moviename in movielist:
    movielist[ite]=str(movielist[ite]).split('png"/>')[1]
    movielist[ite]=str(movielist[ite]).split('</h3>')[0]
    movielist[ite]=str(movielist[ite]).strip()
    if movielist[ite]==movie:
        break
    ite=ite+1
ite=ite+1
divfind=2
lifind=1
stopval=0
timelist = soup.select('#divContent > section:nth-child('+str(ite)+') > div > ul')
print("timelist length:"+str(len(timelist)))

for divfind in range(2,len(timelist)+1):

    timelist2 = soup.select('#divContent > section:nth-child('+str(ite)+') > div:nth-child('+str(divfind)+') > ul > li')

    print("timelist2 length:"+str(len(timelist2))+"divfind="+str(divfind))

    for lifind in range(1,len(timelist2)+1):
        time.sleep(1)
        timelist3 = soup.select('#divContent > section:nth-child('+str(ite)+') > div:nth-child('+str(divfind)+') > ul > li:nth-child('+str(lifind)+')')

        timelist3[0]=str(timelist3[0]).split('">')[1]
        timelist3[0]=str(timelist3[0]).split("</")[0]

        if timelist3[0] == movietime:
            stopval=1
            print("!!!!!!!!")
            break
    if stopval == 1:
        break


driver.find_element_by_xpath('//*[@id="divContent"]/section['+str(ite)+']/div['+str(divfind-1)+']/ul/li['+str(lifind)+']/a').click()

driver.find_element_by_class_name('dialog-confirm').click()

time.sleep(1)
alert=driver.switch_to_alert()
alert.accept()
try:
    time.sleep(1)
    alert=driver.switch_to_alert()
    alert.accept()
except:
    #do nothing
    print("",end='')


time.sleep(1)

driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbUserID').send_keys('sh05158')
driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbPassword').send_keys('songfish320')

driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').click()

driver.find_element_by_xpath('//*[@id="divContent"]/section['+str(ite)+']/div['+str(divfind-1)+']/ul/li['+str(lifind)+']/a').click()

driver.find_element_by_class_name('dialog-confirm').click()

time.sleep(1)

alerts=driver.switch_to_alert()
alerts.accept()

try:
    time.sleep(1)
    alert=driver.switch_to_alert()
    alert.accept()
except:
    #do nothing
    print("",end='')
driver.find_element_by_xpath('//*[@id="General"]/option[2]').click()




html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

seat = soup.select('#seat_table > tbody > tr')
ylength=len(seat)
xlength=0
xpos = 0
ypos = 1

seat2 = soup.select('#seat_table > tbody > tr:nth-child('+str(ypos)+') > td')

seat_result = [["N" for col in range(50)] for row in range(50)]
seat_rating = [["N" for col in range(50)] for row in range(50)]
seat_status = [[-2 for col in range(50)] for row in range(50)]


for ypos in range(1,ylength+1):
    seat2 = soup.select('#seat_table > tbody > tr:nth-child('+str(ypos)+') > td')
    xlength=len(seat2)
    for xpos in range(2,xlength+1):
        
        seat_result[ypos-1][xpos-2]=str(seat2[xpos-2]).split('">')[1]
        seat_result[ypos-1][xpos-2]=str(seat_result[ypos-1][xpos-2]).split("</td>")[0]
        seat_result[ypos-1][xpos-2]=str(seat_result[ypos-1][xpos-2]).strip()
        if seat_result[ypos-1][xpos-2] == "":
            seat_result[ypos-1][xpos-2] = "X"

        tempstatus=str(seat2[xpos-2]).split('reservation="')[1]
        tempstatus=tempstatus.split('" ')[0]
        
        if tempstatus=="Yes":
            seat_status[ypos-1][xpos-2]=1
        elif tempstatus=="No":
            seat_status[ypos-1][xpos-2]=0
        else:
            seat_status[ypos-1][xpos-2]=-1

        tempstatus=str(seat2[xpos-2]).split('rating_nm="')[1]
        tempstatus=tempstatus.split('" ')[0]

        if tempstatus=="Economy석":
            seat_rating[ypos-1][xpos-2]="E"
        elif tempstatus=="Standard석":
            seat_rating[ypos-1][xpos-2]="S"
        elif tempstatus=="Prime석":
            seat_rating[ypos-1][xpos-2]="P"
        else:
            seat_rating[ypos-1][xpos-2]="X"

tempy=0
tempx=0

for tempy in range(0,len(seat_result)):
    for tempx in range(0,len(seat_result[tempy])):
        print(str(seat_result[tempy][tempx]) + " ",end='')
    print(" ")
for tempy in range(0,len(seat_result)):
    for tempx in range(0,len(seat_result[tempy])):
        print(str(seat_rating[tempy][tempx]) + " ",end='')
    print(" ")
for tempy in range(0,len(seat_result)):
    for tempx in range(0,len(seat_result[tempy])):
        print(str(seat_status[tempy][tempx]) + " ",end='')
    print(" ")

time.sleep(10)
