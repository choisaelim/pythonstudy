import os
import subprocess

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
    subprocess.check_output('py -m PyInstaller attend.py --onefile ', shell=True, encoding='utf-8')  
    # subprocess.check_output('pyinstaller attend.py --onefile ', shell=True, encoding='utf-8')  

os.system("pause")