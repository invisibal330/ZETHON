P = '\x1b[1;97m'
import platform
import os
os.system('termux-setup-storage')
#os.system('git pull')
#try:os.system('mkdir /sdcard/PROHACK-DATA')
#except:pass
#try:os.system('mkdir /sdcard/PROHACK-DATA/OK')
#except:pass
#try:os.system('mkdir /sdcard/PROHACK-DATA/CP')
#except:pass
try:os.system('touch .prox.txt')
except:pass
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(P))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("ZETHON").login()
	else:
		__import__("ZETHON").login()
