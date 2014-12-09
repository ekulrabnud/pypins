from flask import Flask, render_template ,request
import datetime
import RPi.GPIO as GPIO

app = Flask(__name__,static_url_path='')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route("/")
def hello():
	pinstate = get_pinstate()
	templateData = {
		'title':'Dunbar PI',
		'pin22' : pinstate['22'],
		'pin23' : pinstate['23'],
		'pin24' : pinstate['24'],
		'pin25' : pinstate['25'],
		}
	
	return render_template("main.html", **templateData)



@app.route("/relay")
def relayi():
	data = request.args
	pin = int(data['pin'])
	try:
		GPIO.output(pin,not GPIO.input(pin)) 
		
		if GPIO.input(pin)==1:
			state = "ON"
		else:
			state = "Off"
	except:
		state = "error" 
	#data = ajaxtemp()
	return state 


def get_pinstate():
	pins = [4,17,27,22,18,23,24,25]
	pinstate = {}
	for i in pins:
		GPIO.setup(i,GPIO.OUT)
		if (GPIO.input(i)):
			pinstate[str(i)] = "ON"
		else: 
			pinstate[str(i)] = "OFF"
  
      #pinstate = json.dumps(pinstate)
	return pinstate

if __name__=='__main__':
 	app.run(host='0.0.0.0',port=8900,debug=True)
