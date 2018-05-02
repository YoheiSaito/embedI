import RPi.GPIO as IO
import time

BUTTON=26
LED= 19
flg = False
freq = 20

def main():
     
#OUTPUT PIN CONFIGURE
    IO.setmode(IO.BCM)
    IO.setup(LED, IO.OUT)

#INPUT PIN CONFIGURE
    IO.setup(BUTTON, IO.IN, pull_up_down=IO.PUD_UP)    
    IO.add_event_detect(BUTTON, IO.FALLING)
    IO.add_event_callback(BUTTON, sw_callback)
    
    for x in range(5):
        risetest()
    for x in range(5):
        falltest()
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

def risetest():
    global freq
    global flg
    freq = 20
    try:
        while True:
            if(flg == False):
                for k in range(0, freq):
                    pwm(freq)
                freq = (freq + 1)
                if (freq == 61) : break
            else :
                break
    except KeyboardInterrupt:
        pass
    flg = False

def falltest():
    global freq
    global flg
    freq = 60
    try:
        while True:
            if(flg == False):
                for k in range(0, freq) :
                    pwm (freq)
                freq = freq - 1
                if (freq == 19) : break
            else :
                break
    except KeyboardInterrupt:
        pass
    flg = False

if __name__ == '__main__':
    main()

