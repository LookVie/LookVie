from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome('/Users/hansn/Documents/chromedriver') #본인 크롬 드라이버 다운 위치에 설정
# https://sites.google.com/a/chromium.org/chromedriver/downloads 에서 설치
driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/Schedule/?tc=0056&t=T&ymd=20190516&src=')
time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#cinema_list = []
#str_cinema = []
#cinema_list=soup.select('#theaterList_01 > ul > li')
s_time1 = soup.select('#divContent > section > div > ul > li > a')
for top1 in s_time1:
    temp = top1
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str0 = str(temp).strip('<>')
        s_time0_2=str0.split('(')
        s_time0_3 = s_time0_2[1].split(',')
        s_temp0 = s_time0_3[17].strip('\'\'') + ' ' +  s_time0_3[1].strip('\'\'') + '\''
        print('CGV강남' + ' ' + s_time0_3[0] + ' ' + s_temp0 + ' ' + s_time0_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[2]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time2 = soup.select('#divContent > section > div > ul > li > a')
for top2 in s_time2:
    temp = top2
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time1_2=str1.split('(')
        s_time1_3 = s_time1_2[1].split(',')
        s_temp1 = s_time1_3[17].strip('\'\'') + ' ' +  s_time1_3[1].strip('\'\'') + '\''
        print('CGV강변' + ' ' + s_time1_3[0] + ' ' + s_temp1 + ' ' + s_time1_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[3]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time3 = soup.select('#divContent > section > div > ul > li > a')
for top3 in s_time3:
    temp = top3
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV건대입구' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[4]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time4 = soup.select('#divContent > section > div > ul > li > a')
for top4 in s_time4:
    temp = top4
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV구로' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[5]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time5 = soup.select('#divContent > section > div > ul > li > a')
for top5 in s_time5:
    temp = top5
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV대학로' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[6]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time6 = soup.select('#divContent > section > div > ul > li > a')
for top6 in s_time6:
    temp = top6
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV동대문' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[7]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time7 = soup.select('#divContent > section > div > ul > li > a')
for top7 in s_time7:
    temp = top7
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV등촌' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[8]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time8 = soup.select('#divContent > section > div > ul > li > a')
for top8 in s_time8:
    temp = top8
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV명동' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[9]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time9 = soup.select('#divContent > section > div > ul > li > a')
for top9 in s_time9:
    temp = top9
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV명동역 씨네라이브러리' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[10]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time10 = soup.select('#divContent > section > div > ul > li > a')
for top10 in s_time10:
    temp = top10
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV목동' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[11]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time11 = soup.select('#divContent > section > div > ul > li > a')
for top11 in s_time11:
    temp = top11
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV미아' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[12]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time12 = soup.select('#divContent > section > div > ul > li > a')
for top12 in s_time12:
    temp = top12
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV불광' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[13]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time13 = soup.select('#divContent > section > div > ul > li > a')
for top13 in s_time13:
    temp = top13
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV상봉' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[14]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time14 = soup.select('#divContent > section > div > ul > li > a')
for top14 in s_time14:
    temp = top14
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV성신여대입구' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[15]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time15 = soup.select('#divContent > section > div > ul > li > a')
for top15 in s_time15:
    temp = top15
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV송파' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[16]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time16 = soup.select('#divContent > section > div > ul > li > a')
for top16 in s_time16:
    temp = top16
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV수유' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[17]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time17 = soup.select('#divContent > section > div > ul > li > a')
for top17 in s_time17:
    temp = top17
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV신촌아트레온' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[18]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time18 = soup.select('#divContent > section > div > ul > li > a')
for top18 in s_time18:
    temp = top18
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV씨네드쉐프 압구정' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[19]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time19 = soup.select('#divContent > section > div > ul > li > a')
for top19 in s_time19:
    temp = top19
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit =1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV씨네드쉐프 용산' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[20]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time20 = soup.select('#divContent > section > div > ul > li > a')
for top20 in s_time20:
    temp = top20
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV압구정' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[21]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time21 = soup.select('#divContent > section > div > ul > li > a')
for top21 in s_time21:
    temp = top21
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV여의도' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[22]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time22 = soup.select('#divContent > section > div > ul > li > a')
for top22 in s_time22:
    temp = top22
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV영등포' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[23]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time23 = soup.select('#divContent > section > div > ul > li > a')
for top23 in s_time23:
    temp = top23
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV왕십리' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[24]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time24 = soup.select('#divContent > section > div > ul > li > a')
for top24 in s_time24:
    temp = top24
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV용산아이파크몰' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[25]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time25 = soup.select('#divContent > section > div > ul > li > a')
for top25 in s_time25:
    temp = top25
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV중계' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[26]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time26 = soup.select('#divContent > section > div > ul > li > a')
for top26 in s_time26:
    temp = top26
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV천호' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[27]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time27 = soup.select('#divContent > section > div > ul > li > a')
for top27 in s_time27:
    temp = top27
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV청담씨네시티' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[28]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time28 = soup.select('#divContent > section > div > ul > li > a')
for top28 in s_time28:
    temp = top28
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV피카디리1958' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[29]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time29 = soup.select('#divContent > section > div > ul > li > a')
for top29 in s_time29:
    temp = top29
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV하계' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])
numbers = 0
driver.find_element_by_xpath('//*[@id="ContainerView"]/section[1]/a').click()
driver.find_element_by_xpath('//*[@id="theaterList_01"]/ul/li[30]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
s_time30 = soup.select('#divContent > section > div > ul > li > a')
for top30 in s_time30:
    temp = top30
    numbers = re.findall("\d+", str(temp))
    if '20190516' in numbers:
        str1 = str(temp).strip('<>')
        s_time_2 = str1.split('(', maxsplit=1)
        s_time_3 = s_time_2[1].split(',')
        s_temp = s_time_3[17].strip('\'\'') + ' ' + s_time_3[1].strip('\'\'') + '\''
        print('CGV홍대' + ' ' + s_time_3[0] + ' ' + s_temp + ' ' + s_time_3[2])