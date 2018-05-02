import RPi.GPIO as gpio
import time
import random

#   A
#   _
# F|_|B _G
# E|_|C .DP
#   D

def main():
    x = 0
    gpio.setmode(gpio.BCM)
    #switch setting
    sw_pin = 26
    gpio.setup(sw_pin,gpio.IN, pull_up_down=gpio.PUD_UP)
    #setting for segment
    # dip 1 to 10
    segment_pins = [7,8,25,24,23,18,15,14]
    segment = SevenSegmentLED(segment_pins)
    try:
        i = 0
        while True:
            x = random.randint(0,9)
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
            self.__io_pins = pin_list
            for x in range(8):
                gpio.setup(self.__io_pins[x], gpio.OUT)

        __pin_to_led = [5, 4, 2, 1, 0, 7, 6, 3]
        __pin_level = [
            [1, 1, 1, 1, 1, 1, 0], #0
            [0, 1, 1, 0, 0, 0, 0], #1
            [1, 1, 0, 1, 1, 0, 1], #2
            [1, 1, 1, 1, 0, 0, 1], #3
            [0, 1, 1, 0, 0, 1, 1], #4
            [1, 0, 1, 1, 0, 1, 1], #5
            [1, 0, 1, 1, 1, 1, 1], #6
            [1, 1, 1, 0, 0, 0, 0], #7
            [1, 1, 1, 1, 1, 1, 1], #8
            [1, 1, 1, 1, 0, 1, 1], #9
            [1, 1, 1, 0, 1, 1, 1], #A
            [0, 0, 1, 1, 1, 1, 1], #B
            [1, 0, 0, 1, 1, 1, 0], #C
            [0, 1, 1, 1, 1, 0, 1], #D
            [1, 0, 0, 1, 1, 1, 1], #E
            [1, 0, 0, 0, 1, 1, 1]  #F
        ]
      
        def out(self,d=0, dp=False):
            if(d < 16) :
                for x in range(7):
                    gpio.output(self.__io_pins[self.__pin_to_led[x]], self.__pin_level[d][x])
            if(dp):
                gpio.output(self.__io_pins[self.__pin_to_led[7]], 1)
            else:
                gpio.output(self.__io_pins[self.__pin_to_led[7]], 0)


main()
