import os
os.system('pip install NamasteiG')
os.system('pip install requests')
os.system('pip install uuid')
os.system('clear')
from NamasteiG import login
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
P = '\u001b[35m'
Y = '\033[1;33m'
W = "\033[0m"
print(G+f'                 IG Session ID Extractor\n{Y}                    S    C    A    P    Y\n')
username = input(P+'Enter Your UserName : ')
password = input(B+'Enter Your PassWord : ')
Data = login.run(username,password).cookies
if 'sessionid' in Data:
	print(Y+'\nYour Session Id > '+G+Data['sessionid'])
else:
	print(R+'Wrong Account')
