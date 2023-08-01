import RPi.GPIO as GPIO
import time
from goto import *
import pio
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
#---CONFIG_BEGIN---
import cpu
import FileStore
import VFP
import Ports

def peripheral_setup () :
# Peripheral Constructors
 pio.cpu=cpu.CPU ()
 pio.storage=FileStore.FileStore ()
 pio.server=VFP.VfpServer ()
 pio.uart=Ports.UART ()
 pio.storage.begin ()
 pio.server.begin (0)
# Install interrupt handlers

def peripheral_loop () :
 pio.server.poll ()

#---CONFIG_END---
# Main function
def main () :
    
   peripheral_setup()
   pio.uart.setup(9600)
   while(1):

    if GPIO.input(18)==GPIO.LOW:
      GPIO.output(4, GPIO.HIGH)
      GPIO.output(17, GPIO.LOW)
      pio.uart.println("Clockwise")
      time.sleep(0.1)
    else:
      GPIO.output(4, GPIO.LOW)
      GPIO.output(17, GPIO.HIGH)
      pio.uart.println("AntiClockwise")
      time.sleep(0.1)  
	 

if __name__ == '__main__' :
   main()  
