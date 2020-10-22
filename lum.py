#!/usr/bin/python3

# a poor man luminosity sensor with digital pins
# a photoresistor is chained with a 47uF capacitor
# we set the voltage to zero and count the time to 
# get a high value again

import RPi.GPIO as GPIO
import time
import statistics

import settings

def get_lum():

   GPIO.setup(settings.PIN, GPIO.OUT)
   GPIO.output(settings.PIN,False)
   time.sleep (0.01)

   GPIO.setup(settings.PIN, GPIO.IN)
   count = 0
   while not GPIO.input(settings.PIN) and count<settings.DARK:
     count += 1
     time.sleep (0.001)
   return count


def median_lum():
   GPIO.setmode(GPIO.BCM)
   m = []
   for i in range(settings.MEASURES):
     m.append ( get_lum() )
   GPIO.cleanup (settings.PIN)
   return statistics.median(m)

if __name__ == "__main__": 
   print (median_lum())

