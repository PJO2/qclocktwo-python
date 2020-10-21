
HORLOGE =  [
        "IL#ESTRUNELDIX" ,
        "MINUITDEUXSEPT" ,
        "QUATREMIDICINQ" ,
        "HUIT-TROISNEUF" ,
        "SIXONZE+HEURES" ,
        "TRENTEQUARANTE" ,
        "VINGTCINQUANTE" ,
        "DIXQUATRESEPTI" ,
        "UNE#TROISSEIZE" ,
        "SIXEPILE!DEUXF" ,
        "ONZELNEUFCHUIT" ,
        "UEDOUZEACINQUE" ,
        "QUATORZETREIZE" ,
        "CQUINZEADEGRES" ,
]


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

import datetime
import os
import time

SIZE = 14
FLAT_HORLOGE = "".join(HORLOGE)

def Replace(txt, date, start_at):
   if start_at==0:
       idx = FLAT_HORLOGE.find( txt )
   else:
       idx = FLAT_HORLOGE.rfind( txt )
   if idx!=-1:
      for ark in range(idx, idx+len(txt)):
         date[ark] = FLAT_HORLOGE[ark]


def Get_Display(heure, minute):
   date = [' '] * SIZE * SIZE

   # for each symbol take the letters from horloge
   for word in HEUREs[heure].split (" "):
      if word != '':
         Replace (word, date, 0)
   for word in MINUTEs[minute].split (" "):
      if word != '':
         Replace (word, date, 5*SIZE)
   return date

def Display(date):
  print ( '_' * (SIZE+2) )
  for raw in range(SIZE):
      print ("".join( ['|'] + date[raw*SIZE:raw*SIZE+SIZE] + ['|'] ) )
  print ( '_' * (SIZE+2) )

if __name__ == "__main__":
    dd = datetime.datetime.now()
    Get_Display(dd.hour, dd.minute)

    for hour in range(17,24):
      for minute in range(60):
         date = Get_Display(hour, minute)
         Display (date)
         time.sleep (1)
         os.system('clear')


