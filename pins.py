
import RPi.GPIO as GPIO
import time

class RPiRelay(object):

	pins = [4,17,27,22,18,23,24,25,]
	GPIO.setmode(GPIO.BCM)
	def __init__(self):
		self.pins = RPiRelay.pins
		self.pinstate = {}
		for i in self.pins:
			GPIO.setup(i,GPIO.OUT)
			if (GPIO.input(i)):
				self.pinstate[str(i)]= 'ON'
			else:
				self.pinstate[str(i)] = 'OFF'

	def get_pinstate(self,pin):
		return self.pinstate[str(pin)]
	def pin_on(self,pin):
		if not GPIO.input(pin):
			GPIO.output(pin,1)
	def pin_off(self,pin):
		if GPIO.input(pin):
			GPIO.output(pin,0)
	def all_on(self):
		for i in self.pins:
			GPIO.output(i,1)
	def all_off(self):
		for i in self.pins:
			GPIO.output(i,0)

	def get_all_pinstate(self):
		for i in self.pins:
			if GPIO.input(i):
				print '%s is ON' % str(i)
			else:
				print '%s is OFF' % str(i)
def test():

	pyrelay = RPiRelay()

	for k,i in pyrelay.pinstate.items():
		print k,i

	print pyrelay.get_pinstate(23)
	pyrelay.pin_on(25)
	pyrelay.pin_off(27)
	pyrelay.all_on()
	#pyrelay.all_off()
	pyrelay.get_all_pinstate()



if __name__ == '__main__':
	test()

