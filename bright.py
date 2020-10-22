#!/usr/bin/python3

# bright the leds according to the actual time


# import neopixle library which does much of the work

import datetime

import settings
import lum
import qclock

import neopixel
import time

def rgb(pos):
   red   = abs ( 128 - pos * ( 256 + 128 ) / settings.nLEDs )
   green = 256 - abs (  256 - pos * ( 128 + 256 ) / settings.nLEDs )
   blue  =  256 - red
   return [ red, green, blue ]

def adjust (rgb, lum):
   a_rgb = [0, 0, 0]
   for i in range(3):
     a_rgb[i] = 1 + rgb[i] * lum / 250
   return a_rgb

# send RGC code the led strip
def dimmed_display_with_offset(pixels, leds, lum):
   for OFFSET in range (14):
     for idx in range(14*OFFSET,14*(OFFSET+1)):
       if leds[idx]:
           pixels [idx-OFFSET*14]=  adjust( rgb (idx), lum )
       else:
           pixels[idx-OFFSET*14] = 0
     time.sleep(2)
     pixels[0] = [ 100,0,0]
     time.sleep(0.01)
     pixels[0] = [ 0,0,0]



# send RGC code the led strip
def dimmed_display(pixels, leds, lum):
   for idx in range(settings.nLEDs):
       if leds[idx]:
           pixels [idx]=  adjust( rgb (idx), lum )
       else:
           pixels[idx] = 0

# ----- 
# main 
# -----

lum = (255-lum.median_lum()) * 10 / settings.LUM      # get current luminosity
dd = datetime.datetime.now()                     # get time
leds = qclock.Get_Display(dd.hour, dd.minute)    # translate time into a 0/1 array


pixels = neopixel.NeoPixel(settings.LEDSTRIP_PIN, settings.nLEDs)
dimmed_display(pixels, leds, lum)             # send RGB code for each 1 in array

