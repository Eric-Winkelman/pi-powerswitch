from flask import Flask
from flask import jsonify
from flask import request

import time
import os
import subprocess
from subprocess import check_output

import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)


@app.route("/toggleSwitch/<rfCode>")
def toggleSwitch(rfCode):
	
	os.system("sudo /eric/codesend " + rfCode)
	return jsonify(success="true", rfCode=rfCode)
	

@app.route("/getCode")
def getCode():	
        #(output, error) = p.communicate()
	
	#output = os.system("sudo /eric/RFSource/RFSniffer")
	
	#output = subprocess.check_output(["sudo", "/eric/RFSource/RFSniffer"])
	
	p = subprocess.Popen(["sudo /eric/EricRFSource/RFSniffer"], stdout=subprocess.PIPE, shell=True)
	returnCode = p.communicate()[0]
	
	return jsonify(success="true", code=str(returnCode))
	

if __name__ == "__main__":
	
	#pin 3 defults to on
	#GPIO.setup(4, GPIO.OUT)
	#GPIO.setup(17, GPIO.OUT)

	#GPIO.output(4, 0)
	#GPIO.output(17, 0)
		

	app.run(host='0.0.0.0', port=80, debug=True)


