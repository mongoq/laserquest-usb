# Laserquest USB

Steuern (auslenken und schalten) des Lasers / der zwei Servos per Cursor-Tasten (Ncurses / Linux) bei USB-Anbindung von einem Arduino Nano

String Position Parser - Arduino empfängt Befehle in der Form ...

**x,y,1** ... z.B. **30,30,1**

... über USB-UART, d.h. **Laser X-Position** - Komma - **Laser Y-Position** - Komma - **Laser an/aus als 1 oder 0** ...

... auch über Terminalprogramm testbar (!)

Baudrate: 9600

X/Y Wertebereich (immer bei Hardwarezusammenstellung ausprobieren ?): Todo

Todo: 
* Bild
* Verkabelung Bild
* Ubuntu Pakete (welche sind nachzuinstallieren für Ncurses Gaming Library (?)) --> **sudo apt-get install python-pygame** (http://www.forum-raspberrypi.de/Thread-python-python-tastendruecke - Testen (!))
