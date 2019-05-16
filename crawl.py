from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome('/Users/hansn/Documents/chromedriver')
driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/Schedule/?tc=0056&t=T&ymd=20190516&src=')
time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
cinema_list = []
cinema_list=soup.select('#theaterList_01 > ul > li')
screen = soup.select('#divContent > section > div > ul > li > a')
s_time = soup.select('#divContent > section > div > ul > li > a')
for topc in cinema_list:
    for top in s_time:
        temp = top
     #   print(temp)
        numbers = re.findall("\d+", str(temp))
        if '20190516' in numbers:
            str1 = str(temp).strip('<>')
            s_time_2=str1.split('(')
            s_time_3 = s_time_2[1].split(',')
            print(topc.text + ' ' + s_time_3[0] + ' ' + s_time_3[17] + ' ' + s_time_3[1] + ' ' + s_time_3[2])


