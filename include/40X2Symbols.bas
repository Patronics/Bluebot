#include "sharedSymbols.bas"

#picaxe 40x2

symbol j21a=A.0
symbol j21b=A.1
symbol j21c=A.2

symbol j22a=C.0
symbol j22b=B.2
symbol j22c=C.7

symbol j23a=A.7
symbol j23b=B.1
symbol j23c=D.4

symbol j24a=A.6
symbol j24b=C.5
symbol j24c=A.3

symbol j25a=A.5
symbol j25b=C.6
symbol j25c=B.0


'...
'Motor control pins
symbol RmotorPWM=C.2   'pwm outputs
symbol LmotorPWM=C.1   'pwm outputs
symbol LmotorDir1=B.6   'D.0  ' B.7    may need reorganizing
symbol LmotorDir2=D.1  ' B.6    may need reorganizing
symbol RmotorDir1=D.2  ' B.5    may need reorganizing
symbol RmotorDir2=D.3  ' B.4    may need reorganizing
'symbol LmotorForward=LmotorDir1
'symbol LmotorReverse=LmotorDir2
'symbol RmotorForward=RmotorDir1
'symbol RmotorReverse=RmotorDir2
''Light Dependent Resistor
symbol ldr1=27     'D.7
symbol ldr2=26     'D.6
symbol ldr3=25     'D.5
'Other I/O
'symbol solenoidDriver=
;symbol gobutton=pinB.0
;symbol fan=C.4
;symbol irSensor=pinC.2
'-----contstants------
;symbol sm=9
;symbol sd=20
;symbol fullspeedtemp=1023*sm
;symbol fullspeed=fullspeedtemp/sd
;symbol halfspeedtemp=512*sm
;symbol halfspeed=halfspeedtemp/sd
;symbol quarterspeedtemp=256*sm
;symbol quarterspeed=quarterspeedtemp/sd
;symbol stopspeed=0

'''LDR Data
'symbol ldrthresh=130
'symbol checkgreater=bit5   ''workaround for if statement bug
'checkgreater=1     
'-----Variables-------
;symbol arg1=b2
;symbol arg2=b3
;symbol argw1=w1
;symbol returnw=w3
;symbol returnw1=returnw
;symbol returnb1=b6
;symbol returnb2=b7
;symbol returnw2=w4
;symbol returnb3=b8
;symbol returnb4=b9
;symbol Fusrfval=w5
;symbol Rusrfval=w6
;symbol Lusrfval=w7
;symbol ldr1val=b16
;symbol ldr2val=b17
;symbol ldr3val=b18
;symbol loopcount=b19
;symbol currentlyturning=bit0
;symbol turningright=bit1
;symbol ldr1on=bit2
;symbol ldr2on=bit3
;symbol ldr3on=bit4
;symbol loopcount2=b20
;symbol timer2=b21
;symbol state=b22
;symbol recentlydoing=b23     ''   | for stopping too many repitions of the same state
;symbol doingduration=b24    ''   |
;symbol olddoing=b25            ''   |
;symbol turnstage=b26
;symbol timesincescan=timer2
;symbol doingmax=5