import os
import RPi.GPIO as GPIO
from flask import Flask, render_template, Response
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

now=datetime.datetime.now()
timeString=now.strftime("%Y-%m-%d %H:%M")
templateData={
	'title':'Raspberry Pi 3B+ Web Controller',
	'time':timeString,
	'data':'pouet',
}


app=Flask(__name__)
	
@app.route('/')
def index():
	#return 'hello world!'
	now=datetime.datetime.now()
	timeString=now.strftime("%Y-%m-%d %H:%M")
	templateData={
		'title':'Raspberry Pi 3B+ Web Controller',
		'time':timeString,
	}
	#return render_template('rpi_index.html',**templateData)
	return render_template('rpi3b_webcontroller.html',**templateData)           

@app.route('/<actionid>') 
def handleRequest(actionid):
	print("Button pressed : {}".format(actionid))
	
	if format(actionid) == 'on':
		GPIO.output(21, GPIO.HIGH)
	elif format(actionid) == 'off':
		GPIO.output(21, GPIO.LOW)
	return "OK 200"   
	                      	
if __name__=='__main__':
	os.system("sudo rm -r  ~/.cache/chromium/Default/Cache/*")
	app.run(debug=True, port=5000, host='0.0.0.0',threaded=True)
	#local web server http://192.168.1.200:5000/
	#after Port forwarding Manipulation http://xx.xx.xx.xx:5000/
