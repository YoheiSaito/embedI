import RPi.GPIO as gpio
import time
import random

#   A
#   _
# F|_|B _G
# E|_|C .DP
#   D

def main():
    gpio.setmode(gpio.BCM)
    #switch setting
    sw_pin = 26
    gpio.setup(sw_pin,gpio.IN, pull_up_down=gpio.PUD_UP)
    #setting for segment
    # A to dp
    segment_pins = [7,8,25,24,23,18,15,14]
    segment = SevenSegmentLED(segment_pins)
    try:
        i = 0
        while True:
            x =  random.randint(0,9)
            segment.out(x, False)
            time.sleep(0.025)
            if(gpio.input(sw_pin) == 0):
                print(x)
                # display and chattering measures
                time.sleep(0.5)
                i = i+1
            if(i == 50) :
                break
    except KeyboardInterrupt:
        pass

    gpio.cleanup()


class SevenSegmentLED():
        def __init__(self, pin_list= []):
            self.io_pins = pin_list
            for x in range(8):
                gpio.setup(self.io_pins[x], gpio.OUT)
    
        __pin_level = [
            [gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW ],
            [gpio.LOW , gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.LOW , gpio.LOW , gpio.LOW ],
            [gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.HIGH],
            [gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.LOW , gpio.HIGH],
            [gpio.LOW , gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.LOW , gpio.HIGH, gpio.HIGH],
            [gpio.HIGH, gpio.LOW , gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.HIGH, gpio.HIGH],
            [gpio.HIGH, gpio.LOW , gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH],
            [gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.LOW , gpio.LOW , gpio.LOW ],
            [gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH],
            [gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW , gpio.HIGH, gpio.HIGH]
        ]
      
        def out(self,d=0, dp=False):
            for x in range(7):
                gpio.output(self.io_pins[x], self.__pin_level[d][x])
            if(dp):
                gpio.output(self.io_pins[7], gpio.HIGH)
            else:
                gpio.output(self.io_pins[7], gpio.LOW)


main()
