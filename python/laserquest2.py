#!/usr/bin/python

import time
import sys
import curses
import serial
import math

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

distance = 10

x_offset = 0
y_offset = 0
key = ''
while key != ord('q'):
    stdscr.refresh()
    #key = stdscr.getch()
    #stdscr.addch(20,25,key)
    key = stdscr.getch()
    output = "Laser"
    if key == curses.KEY_UP:
	output = "Laser up"
        x_offset = 0
        y_offset = -distance
    if key == curses.KEY_DOWN:
	output = "Laser down"
        x_offset = 0
        y_offset = distance
    if key == curses.KEY_LEFT:
	output = "Laser left"
        x_offset = -distance
        y_offset = 0
    if key == curses.KEY_RIGHT:
 	output = "Laser right"     
        x_offset = distance
        y_offset = 0
    if key == ord(' '):
 	output = "Laser center"   
        x_offset = 0
        y_offset = 0
    if key == ord('1'):
        distance = 2
    if key == ord('2'):
        distance = 4
    if key == ord('3'):
        distance = 8
    if key == ord('4'):
        distance = 16
    if key == ord('5'):
        distance = 32
    if key == ord('6'):
        distance = 64
    if key == ord('r'):
	output = "Laser rotate"
	stdscr.addstr(5,0,output) 
	i = 0	
	while i <= 360:
	    x_offset=int((math.cos(i/(2*math.pi)))*40)+90
	    y_offset=int((math.sin(i/(2*math.pi)))*40)+90
	    time.sleep(1)
	    print str(x_offset * 0.1) + " " + str(y_offset * 0.1)
            ser.write(str(round(x_offset*0.1)) + "," + str(round(y_offset*0.1)) + ",1;\r\n")
	    i=i+1
    ser.write(str(60 + x_offset) + "," + str(60 + y_offset) + ",1;\r\n")

    stdscr.move(5,0)
    stdscr.clrtoeol()
    stdscr.addstr(5,0,output)
    stdscr.move(7,0)
    stdscr.clrtoeol()
    stdscr.addstr(7,0,"Distance: " + str(distance))

    #time.sleep(1)
    #ser.flushInput()
    #ser.flushOutput()
curses.endwin()
ser.close()
