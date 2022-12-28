#!/usr/bin/env python
#
# Usage:
# 1. Install dependencies: python(2?), flask, mjpeg-streamer.
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.
from flask import Flask, render_template, Response, request, make_response, redirect
from flask_socketio import SocketIO, send, emit
import eventlet
import time, threading, Queue, os
from threading import Thread, Event
from urlparse import urlparse
import subprocess
from smbus import SMBus

bus = SMBus(1)        #/dev/i2c-1
time.sleep(1)
PICAXE_ADDR = 0x1f     #7 bit address form, will be shifted left


app = Flask(__name__)
app.config['SECRET_KEY'] = 'set secret key here'
socketio = SocketIO(app, async_mode="eventlet")
global mstream
global setspeed
setspeed=100
mstream=subprocess.Popen(["/usr/local/bin/mjpg_streamer",'-i','input_raspicam.so -quality 10 -fps 5 -rot 270', '-o', "output_http.so -p 8888 -w /usr/local/share/mjpg-streamer/www"], stdout=subprocess.PIPE)



@app.route('/')
def overview():
    server=urlparse(request.url)
    mstat = ""
    hv=""
    lv=""
    hvcell=""
    global setspeed
    try:
	hv=bus.read_byte_data(PICAXE_ADDR, 8)/10.0       #technically stored as word variables, but never above 255 anyway, so might as well read a byte
	lv=bus.read_byte_data(PICAXE_ADDR, 10)/10.0
	hvcell=round(hv/3,2)
	if hv>=12:
		overlimit=">="
	else:
		overlimit=""
    except IOError:
       print "Voltage Read Failed"
       hv="error"
       lv="error"
       overlimit="error"
    return render_template('bluebot.html',hostname=server.hostname, time=time.time(), hv=hv, lv=lv, hvcell=hvcell, setspeed=setspeed, overlimit=overlimit)


@app.route('/settings')
def settingspage():
        server=urlparse(request.url)
        return render_template("settings.html",hostname=server.hostname)



@app.route('/shutdown')
def shutdown():
        subprocess.call(["shutdown", "now", "-h"])
        return render_template('settingschange.html')   #TODO: give page explaining what's happening (if shutdown/reboot fails or is slow)
@app.route('/reboot')
def reboot():
        subprocess.call("reboot")
        return render_template('settingschange.html')   #TODO: give page explaining what's happening (if shutdown/reboot fails or is slow)


@app.route('/restart_mjpg')
def restartmjpg():
        #todo actually implement restart
	global mstream
	#subprocess.call(["/usr/bin/pkill", "-f", "mjpg_streamer"])
	mstream.terminate()
	#TODO fix if needed mstream=subprocess.Popen(["/usr/local/bin/mjpg_streamer",'-i','input_uvc.so -r 1280x720 -d /dev/video0 -q 80', '-o', "output_http.so -p 8888 -w /usr/local/share/mjpg-streamer/www"], stdout=subprocess.PIPE)
	time.sleep(0.1)
	if (mstream.poll()!=None):
		print "error: mjpg_streamer died with this output:\n"
		print mstream.communicate()
	return render_template('settingschange.html')


@app.route('/stream')
def index():
    server=urlparse(request.url)
    return render_template('index.html',hostname=server.hostname)

@app.route('/video_feed')
def video_feed():
    server=urlparse(request.url)
    return redirect("http://"+server.hostname+":8888/stream_simple.html",302)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('go')
def go(speed,dir):
	#print request.args
	#time.sleep(1)
	print ("going with speed", speed, " and dir", dir)
	global setspeed
	setspeed=int(speed)  #int(request.args["speed"])
	#dir=int(request.args["direction"])
	if dir > 2:
		#slow down for turns
		bus.write_byte_data(0x1f,5, setspeed/2)
	else:
		bus.write_byte_data(0x1f,5, setspeed)

	bus.write_byte_data(0x1f,6,int(dir))
	#bus.write_byte_data(0x1f,6, int(dir)
	#return render_template("settingschange.html")


if __name__ == '__main__':
	
	bus.write_byte_data(PICAXE_ADDR, 0x01, 0x10)
	socketio.run(app,host='0.0.0.0', debug=True,use_reloader=False) 
