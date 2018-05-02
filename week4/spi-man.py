import spidev
import time
from decimal import Decimal

spi = spidev.SpiDev()
spi.open(0,0)
spi.bits_per_word = 8
spi.max_speed_hz = 1000000

start = 0x40
sgl = 0x20
ch0 = 0x00
ch1 = 0x10
msbf = 0x08

def mcp3002(ch):
	rcv=spi.xfer2([(start+sgl+ch+msbf),0x00])
	ad = (((rcv[0]&0x03)<<8)+ rcv[1])
	return ad

try :
	while True:
		print(mcp3002(ch1))
		time.sleep(0.5)
except KeyboardInterrupt:
	pass
spi.close()
