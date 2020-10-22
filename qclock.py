#!/usr/bin/python3

# display the LEDs according to the time and the following matrix
# the RGB code sent to the led trsip is depending on the led position


import datetime
import settings

# how to display each hours starting at 0
HEUREs = [
     "MINUIT"         ,
     "UNE    HEURE"   ,
     "DEUX   HEURES"  ,
     "TROIS  HEURES"  ,
     "QUATRE HEURES"  ,
     "CINQ   HEURES"  ,
     "SIX    HEURES"  ,
     "SEPT   HEURES"  ,
     "HUIT   HEURES"  ,
     "NEUF   HEURES"  ,
     "DIX    HEURES"  ,
     "ONZE   HEURES"  ,
     "MIDI"           ,
     "UNE    HEURE"   ,
     "DEUX   HEURES"  ,
     "TROIS  HEURES"  ,
     "QUATRE HEURES"  ,
     "CINQ   HEURES"  ,
     "SIX    HEURES"  ,
     "SEPT   HEURES"  ,
     "HUIT   HEURES"  ,
     "NEUF   HEURES"  ,
     "DIX    HEURES"  ,
     "ONZE   HEURES"  ,
]

# how to display each minutes starting at 0
MINUTEs = [
       "PILE!"                ,
       "UNE"                  ,
       "DEUX"                 ,
       "TROIS"                ,
       "QUATRE"               ,
       "CINQ"                 ,
       "SIX"                  ,
       "SEPT"                 ,
       "HUIT"                 ,
       "NEUF"                 ,
       "DIX"                  ,
       "ONZE"                 ,
       "DOUZE"                ,
       "TREIZE"               ,
       "QUATORZE"             ,
       "QUINZE"               ,
       "SEIZE"                ,
       "DIX      -  SEPT"     ,
       "DIX      -  HUIT"     ,
       "DIX      -  NEUF"     ,
       "VINGT"                ,
       "VINGT      ET  UN"    ,
       "VINGT      DEUX"      ,
       "VINGT      TROIS"     ,
       "VINGT      QUATRE"    ,
       "VINGT      CINQ"      ,
       "VINGT      SIX"       ,
       "VINGT      SEPT"      ,
       "VINGT      HUIT"      ,
       "VINGT      NEUF"      ,
       "TRENTE"               ,
       "TRENTE     ET    UN"  ,
       "TRENTE     DEUX"      ,
       "TRENTE     TROIS"     ,
       "TRENTE     QUATRE"    ,
       "TRENTE     CINQ"      ,
       "TRENTE     SIX"       ,
       "TRENTE     SEPT"      ,
       "TRENTE     HUIT"      ,
       "TRENTE     NEUF"      ,
       "QUARANTE"             ,
       "QUARANTE   ET    UN"  ,
       "QUARANTE   DEUX"      ,
       "QUARANTE   TROIS"     ,
       "QUARANTE   QUATRE"    ,
       "QUARANTE   CINQ"      ,
       "QUARANTE   SIX"       ,
       "QUARANTE   SEPT"      ,
       "QUARANTE   HUIT"      ,
       "QUARANTE   NEUF"      ,
       "CINQUANTE"            ,
       "CINQUANTE  ET  UN"    ,
       "CINQUANTE  DEUX"      ,
       "CINQUANTE  TROIS"     ,
       "CINQUANTE  QUATRE"    ,
       "CINQUANTE  CINQ"      ,
       "CINQUANTE  SIX"       ,
       "CINQUANTE  SEPT"      ,
       "CINQUANTE  HUIT"      ,
       "CINQUANTE  NEUF"      ,
]
 
 
SIZE = 14
# convert the matrix into a single string
FLAT_HORLOGE = "".join(settings.HORLOGE)

# set True for each index in the matrix which match "txt"
#  works by finding the word "txt" into the matrix
#  and bright len(txt) from the position
def Filter(txt, leds, start_at):
   if start_at==0:
       idx = FLAT_HORLOGE.find( txt )
   else:
       idx = FLAT_HORLOGE.rfind( txt )
   if idx!=-1:
      for ark in range(idx, idx+len(txt)):
         leds[ark] = True


# convert the heure and minute params into an array of word
# then call Display to display each single word
# 5*SIZE is the beginning of the minute matrix
def Get_Display(heure, minute):
   leds = [False] * SIZE * SIZE  # create an empty array

   # for each symbol take the letters from horloge
   for word in HEUREs[heure].split (" "):
      if word != '': 
         Filter (word, leds, 0)
   for word in MINUTEs[minute].split (" "):
      if word != '': 
         Filter (word, leds, 5*SIZE)
   return leds

if __name__ == "__main__":
    dd = datetime.datetime.now()
    leds = Get_Display(dd.hour, dd.minute)
    print (leds)

# extra for testing
    for hour in range(24):
      for minute in range(60):
         leds = Get_Display(hour, minute)
         Display (leds)
      

