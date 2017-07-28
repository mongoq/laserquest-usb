#!/usr/bin/python

import time
import sys
import curses
import serial

# Seriell 
#ser = serial.Serial(
#	port='/dev/ttyUSB0',
#	baudrate=9600,
#	parity=serial.PARITY_ODD,
#	stopbits=serial.STOPBITS_TWO,
#	bytesize=serial.SEVENBITS
#)


#initialization and open the port

#possible timeout values:

#    1. None: wait forever, block call

#    2. 0: non-blocking mode, return immediately

#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()
ser.port = "/dev/ttyUSB3"
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
#ser.timeout = None          #block read
#ser.timeout = 0             #non-block read
ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 5     #timeout for write

try: 

    ser.isOpen()

except Exception, e:

    print "error open serial port: " + str(e)

    exit()


try: 
    ser.open()
except Exception, e:
    print "Error open serial port: " + str(e)
    ser.close()
    exit()


#NCurses ab hier

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,0,"Welcome to Laserquest!")
stdscr.addstr(1,0,"----------------------")
stdscr.addstr(2,0,"")
stdscr.addstr(3,0,"Press 'q' to quit!")
stdscr.addstr(4,0,"")

#print "Welcome to Laserquest!"

#https://docs.python.org/2/library/curses.html

ser.flushInput() #flush input buffer, discarding all its contents
ser.flushOutput()#flush output buffer, aborting current output 

key = ''
while key != ord('q'):
    stdscr.refresh()
    #key = stdscr.getch()
    #stdscr.addch(20,25,key)
    key = stdscr.getch()
    output = "key"
    if key == curses.KEY_UP:
	output = "Laser up"
	ser.write("60,50,1;\r\n")
    if key == curses.KEY_DOWN:
	output = "Laser down"
	ser.write("60,70,1;\r\n")
    if key == curses.KEY_LEFT:
	output = "Laser left"
	ser.write("50,60,1;\r\n")
    if key == curses.KEY_RIGHT:
 	output = "Laser right"        
	ser.write("70,60,1;\r\n")
    if key == ord(' '):
 	output = "Laser center"        
	ser.write("60,60,1;\r\n")
    stdscr.move(5,0)
    stdscr.clrtoeol()
    stdscr.addstr(5,0,output)
    #time.sleep(1)
    #ser.flushInput()
    #ser.flushOutput()
curses.endwin()
ser.close()
