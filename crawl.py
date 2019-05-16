import pymysql

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import string
from datetime import datetime

db = pymysql.connect(host='lookvies.c4gfbjjoxspj.us-east-2.rds.amazonaws.com',port=3306,user='lookvie',passwd='lookvie1234',db='lookvie',charset='utf8')

cursor = db.cursor()

sql = '''
        DROP TABLE timetable
        '''

cursor.execute(sql)

sql = '''
         CREATE TABLE timetable (
  pri_key INT NOT NULL,
  cinema VARCHAR(35) NOT NULL,
  movie VARCHAR(35) NOT NULL,
  screen VARCHAR(35) NOT NULL,
  time VARCHAR(35) NOT NULL,
  PRIMARY KEY (pri_key)
);
        '''

cursor.execute(sql)

cursor.execute('''ALTER TABLE timetable MODIFY COLUMN cinema VARCHAR(35) CHARACTER SET utf8 COLLATE utf8_general_ci''')
cursor.execute('''ALTER TABLE timetable MODIFY COLUMN movie VARCHAR(35) CHARACTER SET utf8 COLLATE utf8_general_ci''')
cursor.execute('''ALTER TABLE timetable MODIFY COLUMN screen VARCHAR(35) CHARACTER SET utf8 COLLATE utf8_general_ci''')
if datetime.today().month<10:
    tempmonth='0'+str(datetime.today().month)
else:
    tempmonth=str(datetime.today().month)

if datetime.today().day<10:
    tempday='0'+str(datetime.today().day+1)
else:
    tempday=str(datetime.today().day+1)

today=str(datetime.today().year)+tempmonth+tempday

cinemalist = ['강남','강변','건대입구','구로','대학로','동대문','등촌','명동','명동역 씨네라이브러리','목동','미아','불광','상봉','성신여대입구','송파','수유','신촌아트레온','씨네드쉐프 압구정','씨네드쉐프 용산','압구정','여의도','영등포','왕십리','용산아이파크몰','중계','천호','청담씨네시티','피카디리1958','하계','홍대']
driver=webdriver.Chrome('/Users/songsari/Desktop/chromedriver')

# https://sites.google.com/a/chromium.org/chromedriver/downloads 에서 설치
driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/Schedule/?tc=0056&t=T&ymd='+today+'&src=')
time.sleep(1)
tempnum = 0
pri_key = 0
for cinemaname in cinemalist:

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    s_time1 = soup.select('#divContent > section > div > ul > li > a')
    for top1 in s_time1:
        temp = top1
        numbers = re.findall("\d+", str(temp))
        if today in numbers:
            str0 = str(temp).strip('<>')
            s_time0_2 = str0.split('(', maxsplit=1)
            s_time0_3 = s_time0_2[1].split(',')
            s_temp0 = s_time0_3[17].strip('\'\'') + ' ' +  s_time0_3[1].strip('\'\'') + '\''
            
            s_time0_3[0]=s_time0_3[0].split("'")[1]
            s_temp0=s_temp0.split("'")[1]
            s_time0_3[2]=s_time0_3[2].split("'")[1]

            print('CGV'+cinemaname + ' ' + s_time0_3[0] + ' ' + s_temp0 + ' ' + s_time0_3[2])
            print(s_time0_3[0])
            cursor.execute("""INSERT INTO timetable (pri_key,cinema,movie,screen,time) VALUES(%s,%s,%s,%s,%s)""",(pri_key,"CGV"+cinemaname,s_time0_3[0],s_temp0,s_time0_3[2]))
            pri_key=pri_key+1
    numbers = 0
    if tempnum==29:
        break
    driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
    driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li['+str(tempnum+2)+']/a').click()
    tempnum= tempnum+1
    time.sleep(1)

db.commit()

db.close()
