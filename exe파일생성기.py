import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import socket

print('input id : ')
idtxt = input()
print('input password : ')
pwd = input()

if idtxt != '' and pwd != '':
    f = open('userinfo.py', 'w')
    f.write('idtxt = ')
    f.write(idtxt)
    f.write('\n')
    f.write('pwd = ')
    f.write(pwd)
    f.close()
    print('id : ', idtxt, 'register OK')
    subprocess.check_output('pyinstaller attend.py --onefile ', shell=True, encoding='utf-8')  
    # subprocess.check_output('pyinstaller attend.py --onefile ', shell=True, encoding='utf-8')  

os.system("pause")

#py -m PyInstaller  exe파일생성기.py --onefile --add-data 'attend.py;.'
#py -m PyInstaller  exe파일생성기.py --add-data 'attend.py;.'