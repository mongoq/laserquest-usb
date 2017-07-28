import time
import sys
import curses

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")

key = ''

while key != ord('q'):
    stdscr.refresh()
    #key = stdscr.getch()
    #stdscr.addch(20,25,key)
    key = stdscr.getch()
    if key == curses.KEY_UP:
	print "KEYUP "
    if key == curses.KEY_DOWN:
	print "KEYDOWN "
    if key == curses.KEY_LEFT:
	print "KEYLEFT "
    if key == curses.KEY_RIGHT:
 	print "KEYRIGHT "        
curses.endwin()
