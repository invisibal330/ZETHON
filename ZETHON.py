
import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("ZETHON32").keyx()
elif 'aarch' in arc:
	__import__("ZETHON").keyx()
else:
	exit(f' Unknow device machine {arc}')
