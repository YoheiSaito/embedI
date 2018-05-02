#16T2806E

import RPi.GPIO as GPIO
import time

CMP=26
LED=19
SWT=13


def main():

	GPIO.setmode(GPIO.BCM)
	#OUTPUT PIN CONFIGURE
	GPIO.setup(LED, GPIO.OUT)
	#INPUT PIN CONFIGURE
	GPIO.setup(CMP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	GPIO.setup(SWT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(CMP, GPIO.BOTH, callback=cmp_callback, bouncetime = 200)
	GPIO.output(LED, GPIO.LOW)
	try:
		while True:
			if (GPIO.input(SWT)==0):
				GPIO.output(LED, GPIO.LOW)
	except KeyboardInterrupt:
		GPIO.cleanup()

def cmp_callback(pin):
	if(GPIO.input(pin) == 1):
		GPIO.output(LED, GPIO.HIGH)
	else:
		pass
main()
