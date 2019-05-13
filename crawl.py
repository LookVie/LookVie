from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('/Users/hansn/Documents/chromedriver')
driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/Schedule/?tc=0001&t=T&ymd=20190513&src=')
time.sleep(1)
#driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbUserID').send_keys('hansnam1105')
#driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbPassword').send_keys('gaza7179!')
#driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
cinema_list=soup.select('#theaterList_01 > ul')
movie = soup.select('#divContent > section > h3')
screen = soup.select('#divContent > section > div > p')
s_time = soup.select('#divContent > section > div:nth-child(2) > ul > li > a')
#divContent > section > div:nth-child(2) > ul > li:nth-child(2) > a
#divContent > section:nth-child(5) > div:nth-child(2)
#divContent > section:nth-child(5) > div:nth-child(2) > ul
for top1 in cinema_list:
    print(top1.text)
    for top2 in movie:
      print(top2.text)
      for top3 in screen:
          print(top3.text)
          for top4 in s_time:
              print(top4.text)

