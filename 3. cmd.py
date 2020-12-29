#cmd 실행
import os
import subprocess
#subprocess
#https://docs.python.org/3/library/subprocess.html

subprocess.check_output('py -m PyInstaller 2. writefile.py --onefile ', shell=True, encoding='utf-8') 
