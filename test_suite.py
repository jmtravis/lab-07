import unittest



import time 
import Adafruit_GPIO 
import Adafruit_GPIO.SPI as SPI
import Adafruit_GPIO.Platform as Platform


import RPi.GPIO as GPIO


import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)


# Software SPI configuration:
# CLK  = 18
# MISO = 23
# MOSI = 24
# CS   = 25
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.

# Main program loop.
 
light_threshold = 100

sound_threshold = 500

while True:
    print("LED Blinking 5 Times")
    for i in range (0,5):
        GPIO.output(11, True)
        time.sleep(0.5)
        GPIO.output(11, False)
        time.sleep(0.5)

    print("Reading light")
    for i in range(0,5):
        light = mcp.read_adc(0)
        
        if (light  > light_threshold):
            print(light, "Bright")
        else:
            print(light, "Dark")
        
        time.sleep(0.1)
    
    print("Blinking 4 times")
    for i in range (0,4):
        GPIO.output(11, True)
        time.sleep(0.2)
        GPIO.output(11, False)
        time.sleep(0.2)
        
    print("Sound Sensor")
    for i in range (0,5):
        sound = mcp.read_adc(1)
        if(sound > sound_threshold):
            print(sound)
            GPIO.output(11, True)
            time.sleep(0.1)
            GPIO.output(11, False)
            time.sleep(0.1)
        else:
            print(sound)
