
import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("ZETHON32").login()
elif 'aarch' in arc:
	__import__("ZETHON").login()
else:
	exit(f' Unknow device machine {arc}')
