import RPi.GPIO as IO
import time

BUTTON=26
LED= 19
flg = False
freq = 20

def main():
    global flg 
    global freq 
#OUTPUT PIN CONFIGURE
    IO.setmode(IO.BCM)
    IO.setup(LED, IO.OUT)

#INPUT PIN CONFIGURE
    IO.setup(BUTTON, IO.IN, pull_up_down=IO.PUD_UP)    
    IO.add_event_detect(BUTTON, IO.FALLING)
    IO.add_event_callback(BUTTON, sw_callback)
    try:
        while True:
            if(flg == False):

                for k in range (0, freq):
                    pwm(freq)
                freq = (freq + 1)
                if(freq == 61) : freq =20
            else :
                break
    except KeyboardInterrupt:
        pass  
    IO.output(LED, IO.HIGH)
    IO.cleanup()

def sw_callback(pin):
    global flg
    global freq
    flg = True
    print (freq)

    
def none():
    pass

def pwm(f):
    IO.output(LED, IO.LOW)
    time.sleep(0.5/f)
    IO.output(LED, IO.HIGH)
    time.sleep(0.5/f)

if __name__ == '__main__':
    main()

