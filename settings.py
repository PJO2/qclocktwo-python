# settings for qclock
import board

LUM = 40	# higher values make clock darker


# Led strip 
nLEDs=196
LEDSTRIP_PIN=board.D18

# GPIO PIN for luminosity
PIN = 4      # use GPIO4
DARK = 250   # darkest value returned by lum
MEASURES=5   # do it 5 times to have a robust value

# The horloge Matrix
HORLOGE =  [
        "IL#ESTRUNELDIX" ,
        "MINUITDEUXSEPT" ,
        "QUATREMIDICING" ,
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

