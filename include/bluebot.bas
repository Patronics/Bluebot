'Main Program for v2 of the FireFighter Bot
'written by Patrick Leiser, [insert your name here], ...
'and the rest of the firebot team in Sierra College Robotics Club [Team]

goto start

#include "include/40X2Symbols.bas"
#include "include/sensorRoutines.bas"
#include "include/motorRoutines.bas"
start:
   '''To consider: worth making a setup.bas include file? or keep in main file?
''hi2csetup i2cmaster, slaveaddr, i2cfast, i2cbyte
'setfreq m16
hi2csetup i2cslave, slaveaddr
'sertxd("i2c enabled!")
symbol speedptr=5
symbol dirptr=6

symbol speed=b5
symbol dir=b6
 gosub setupmotors


main:
pause 200

get speedptr, speed
get dirptr, dir
'toggle A.4
'sertxd("speed=",#speed, "dir=", #dir, cr, lf)

on dir gosub idlestop, goforward, gobackward, turnright, turnleft,steerleft, steerright

arg1=speed
gosub setspeed




goto main: