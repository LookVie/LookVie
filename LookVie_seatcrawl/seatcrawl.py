#프로그램 실행 인자 : seatcrawl 영화관 영화명 상영관 영화시간
# ex : seatcrawl "CGV강남" "어벤져스-엔드게임" "2D | LG gram[5관] 10층" "21:30"


from selenium import webdriver
from bs4 import BeautifulSoup
import time

cinema="CGV 강남"
movie="어벤져스-엔드게임"
screen="2D | LG gram[5관] 10층"
movietime="21:30"

driver=webdriver.Chrome('/Users/songsari/Desktop/chromedriver')

driver.implicitly_wait(3)
driver.get('http://m.cgv.co.kr/WebAPP/Member/Login.aspx?RedirectURL=http://m.cgv.co.kr/quickReservation/default.aspx')

time.sleep(1)
driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbUserID').send_keys('sh05158')
driver.find_element_by_name('ctl00$mainContentPlaceHolder$Login$tbPassword').send_keys('songfish320')

driver.find_element_by_xpath('//*[@id="ContainerView"]/div/div/div/div[1]/div[5]/button').click()
driver.find_element_by_xpath('//*[@id="strTheaterli"]').click()

time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
