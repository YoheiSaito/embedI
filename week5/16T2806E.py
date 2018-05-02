
#16T2806E
import spidev
import time
import pigpio


def main():

        #initialize about adc
        ch0 = 0x00
        ch1 = 0x10
        spi = spidev.SpiDev()
        spi.open(0, 0)
        spi.bits_per_word = 8
        spi.max_speed_hz = 1000000
        
        #initialize about pwm
        PIN = 12
        pi = pigpio.pi()
        pi.set_mode(PIN, pigpio.OUTPUT)

        try :
                for x in range(1,1000):
                        sum = 0.0
                        dtr =  x*1000000//1000
                        pi.hardware_PWM(PIN, 10000, dtr)
                        time.sleep(0.6)
                        for i in range(50):
                                time.sleep(0.01)
                                tmp = mcp3002(spi,ch0)
                                sum += tmp
                        print(str(dtr/1000000.0) +"\t" +str(sum/50.0))
        except KeyboardInterrupt:
                pass
        spi.close()
        pi.stop()


def mcp3002(spi,ch):
        start = 0x40
        sgl = 0x20
        msbf = 0x08
        rcv = spi.xfer2([(start+sgl+ch+msbf), 0x00])
        ad = (((rcv[0] & 0x03) << 8) + rcv[1])
        return ad

main()
