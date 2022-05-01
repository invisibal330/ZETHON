import os,platform

comb =platform.architecture()[0]

if __name__ == "__main__":
	os.system("git pull")
	if comb == "64bit":
		__import__("ZETHON").login()
	elif comb == "32bit":
		__import__("ZETHON64").login()
	else:
		print("UNKNOWN SYSTEM ")
		exit()
