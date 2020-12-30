from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from userinfo import idtxt, pwd
from msg import success_msg, fail_msg
import datetime
import os
import socket

url = 'http://pms.tsb.co.kr/'

framename = 'frame3'
idbox = 'input[name="dlfma"]'
passbox = 'input[name="dkagh"]'
loginbox = '#Table_01 > tbody > tr > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > label'
logoutbox = 'body > div:nth-child(3) > table:nth-child(1) > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2) > label:nth-child(15)'
outbox = 'body > div:nth-child(3) > table:nth-child(3) > tbody > tr > td:nth-child(1) > table:nth-child(5) > tbody > tr > td > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
validation = False

def login_logout(index) :
    try: 
        driver.get(url)
        driver.switch_to.frame(driver.find_element_by_name(framename))

        driver.find_element_by_css_selector(idbox).send_keys(idtxt)
        driver.find_element_by_css_selector(passbox).send_keys(pwd)
        driver.find_element_by_css_selector(loginbox).click()

        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, logoutbox)
            )
        )

        tmpTime = driver.find_element_by_css_selector(outbox).text
        idx = tmpTime.find('퇴근')
        now = datetime.datetime.now()
        three_hour_before = now - datetime.timedelta(hours=3)

        if index == 0:
            if idx != -1 :
                tmp = tmpTime[7:idx].replace(':', '')
                #출근 안한 날 컴퓨터가 켜져 있어 자동으로 실행되면 출근 시간이 방금으로 찍히므로 이런 경우 로그아웃 안하고 종료(Validation false)
                tmpNow = "{:%H}".format(three_hour_before) + "{:%M}".format(three_hour_before) + "{:%S}".format(three_hour_before)
                validation = int(tmp) < int(tmpNow)

            if validation == True : 
                driver.find_element_by_css_selector(logoutbox).click()

                WebDriverWait(driver, 3).until(
                    EC.alert_is_present()
                )

                #alert 창 닫기
                alert = driver.switch_to.alert
                alert.accept()

            else :   
                print(fail_msg)
                print('출근 시간이 퇴근 시간의 3시간 이내입니다')
                driver.close()

        if index == 1:
            tmpTime = driver.find_element_by_css_selector(outbox).text
            outTime = tmpTime[idx + 7:idx + 9]
            
            #퇴근 시간이 18시 이후이면 success! 메세지 출력
            if int(outTime) >= 18 :
                print(success_msg)
            else :
                print(fail_msg)
            driver.close()
    except:
        print(fail_msg)
        print('Attendance Check failed! User IP address : ', socket.gethostbyname(socket.gethostname()))
        driver.close()

for i in range(0, 2):
    login_logout(i)

#실행 결과 확인을 위해 콘솔창 유지
os.system("pause")