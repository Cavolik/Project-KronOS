#KronOS Screen 1.0 Base code
#TO DO: Change screen
import time
import configparser
from luma.lcd.device import hd44780
from luma.core.interface.parallel import bitbang_6800

#Set screen
interface = bitbang_6800(RS=11, E=17, PINS=[27, 22, 10, 9])
device = hd44780(interface, width=20, height=4)


l1 = "X                  X"
l2 = "   Loading KronOS   "
l3 = "  <>                "
l4 = "X                  X"
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <==>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <====>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <======>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <========>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <==========>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <============>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <==============>"
time.sleep(1)
device.text = '\n'.join([l1, l2, l3, l4])
l3 = "  <================>"
time.sleep(2.5)


config = configparser.ConfigParser()

while True:
    for I in range (7):
        #Recive data from clock and radio
        config.read('alarm.ini')
        config.read('radio.ini')

        #Print data
        l1 = config["ALARM"]["lin1"]
        l2 = config["ALARM"]["lin2"] 
        l3 = "Now playing: "
        l4 = config["RADIO"]["playing"]
        device.text = '\n'.join([l1, l2, l3, l4])
        time.sleep(1)
