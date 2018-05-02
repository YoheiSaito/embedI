import RPi.GPIO as GPIO
import time
import math
startTime = time.time()

def main():
	
	cathodes = [16,20,21]
	numpins = [6,13,19,26]

	GPIO.setmode(GPIO.BCM)
	setup_74HC4511(numpins, cathodes)

	try:
		while True:
			t = time.time() - startTime
			displayTime(t, numpins, cathodes)
	except KeyboardInterrupt:
		pass  
	GPIO.cleanup()

def displayTime(t, pins, caths, delay=0.02):
	t = int(t)

	disp = (int(t)//60) % 10
	blnk = (disp == 0)
	output_74HC4511(disp,pins, caths, 2, blnk)
	time.sleep(0.002)

	disp = (int(t)%60 // 10)
	if (disp != 0):
		blnk = False
	output_74HC4511(disp, pins, caths, 1, blnk)
	time.sleep(0.002)

	disp = int(t)%10
	output_74HC4511(disp, pins, caths, 0)
	time.sleep(0.002)

def setup_74HC4511(pins,cothodes):
	for p in cothodes:
		GPIO.setup(p, GPIO.OUT)
		GPIO.output(p, GPIO.HIGH)
	for p in pins:
		GPIO.setup(p, GPIO.OUT)

def output_74HC4511( d, pins, caths,n, blank=False):
	
	if (blank):
		d = 10
	for p in caths:
		GPIO.output(p, 1)
	GPIO.output(caths[n], 0)
	for i in range(len(pins)):
		GPIO.output(pins[i], d%2)
		d = d//2
main()

