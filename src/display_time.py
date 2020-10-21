# Affichage de l'heure

import datetime

# symbols :
OUTPUTs = {
    "_"         : '' ,
    "H_UNE"     : "une",
    "H_DEUX"    : "deux",
    "H_TROIS"   : "trois",
    "H_QUATRE"  : "quatre",
    "H_CINQ"    : "cinq",
    "H_SIX"     : "six",
    "H_SEPT"    : "sept",
    "H_HUIT"    : "huit",
    "H_NEUF"    : "neuf",
    "H_DIX"     : "dix",
    "H_ONZE"    : "onze",
    "H_MIDI"    : "midi",
    "H_MINUIT"  : "minuit",
    "H_HEURE"   : "heure",
    "H_HEURES"  : "heures",

    "M_PILE"    : "pile",
    "M_UNE"     : "une",
    "M_DEUX"    : "deux",
    "M_TROIS"   : "trois",
    "M_QUATRE"  : "quatre",
    "M_CINQ"    : "cinq",
    "M_SIX"     : "six",
    "M_SEPT"    : "sept",
    "M_HUIT"    : "huit",
    "M_NEUF"    : "neuf",
    "M_DIX"     : "dix",
    "M_ONZE"    : "onze",
    "M_DOUZE"   : "douze",
    "M_TREIZE"  : "treize",
    "M_QUATORZE" :"quatorze",
    "M_QUINZE"  : "quinze",
    "M_SEIZE"   : "seize",

    "M_VINGT"   : "vingt",
    "M_TRENTE"  : "trente",
    "M_QUARANTE": "quarante",
    "M_CINQUANTE" : "cinquante",
    "M_TIRET"   : "-",
    "M_UN"      : "un",
    "M_ET"      : "et"
 }




HEUREs = [
   [  "H_MINUIT"   ],
   [  "H_UNE",    "H_HEURE"  ],
   [  "H_DEUX",   "H_HEURES"   ],
   [  "H_TROIS",  "H_HEURES"  ],
   [  "H_QUATRE", "H_HEURES"  ],
   [  "H_CINQ",   "H_HEURES"   ],
   [  "H_SIX",    "H_HEURES"  ],
   [  "H_SEPT",   "H_HEURES"  ],
   [  "H_HUIT",   "H_HEURES"   ],
   [  "H_NEUF",   "H_HEURES"  ],
   [  "H_DIX",    "H_HEURES"  ],
   [  "H_ONZE",   "H_HEURES"  ],
   [  "H_MIDI"    ],
   [  "H_UNE",    "H_HEURE",  ],
   [  "H_DEUX",   "H_HEURES"   ],
   [  "H_TROIS",  "H_HEURES"  ],
   [  "H_QUATRE", "H_HEURES"  ],
   [  "H_CINQ",   "H_HEURES"   ],
   [  "H_SIX",    "H_HEURES"  ],
   [  "H_SEPT",   "H_HEURES"  ],
   [  "H_HUIT",   "H_HEURES"   ],
   [  "H_NEUF",   "H_HEURES"  ],
   [  "H_DIX",    "H_HEURES"   ],
   [  "H_ONZE",   "H_HEURES"  ],

]

MINUTEs = [
     [  "M_PILE"  ],
     [  "M_UNE"  ],
     [  "M_DEUX"  ],
     [  "M_TROIS"  ],
     [  "M_QUATRE"  ],
     [  "M_CINQ"  ],
     [  "M_SIX"  ],
     [  "M_SEPT"  ],
     [  "M_HUIT"  ],
     [  "M_NEUF"  ],
     [  "M_DIX"  ],
     [  "M_ONZE"  ],
     [  "M_DOUZE"  ],
     [  "M_TREIZE"  ],
     [  "M_QUATORZE"  ],
     [  "M_QUINZE"  ],
     [  "M_SEIZE"  ],
     [  "M_DIX",        "M_TIRET,"      "M_SEPT"  ],
     [  "M_DIX",        "M_TIRET,"      "M_HUIT"   ],
     [  "M_DIX",        "M_TIRET,"      "M_NEUF"   ],
     [  "M_VINGT"  ],
     [  "M_VINGT",      "M_ET,"         "M_UN"    ],
     [  "M_VINGT",      "M_DEUX"  ],
     [  "M_VINGT",      "M_TROIS"  ],
     [  "M_VINGT",      "M_QUATRE"  ],
     [  "M_VINGT",      "M_CINQ"  ],
     [  "M_VINGT",      "M_SIX"  ],
     [  "M_VINGT",      "M_SEPT"  ],
     [  "M_VINGT",      "M_HUIT"  ],
     [  "M_VINGT",      "M_NEUF"  ],
     [  "M_TRENTE"  ],
     [  "M_TRENTE",     "M_ET,"         "M_UN"  ],
     [  "M_TRENTE",     "M_DEUX"  ],
     [  "M_TRENTE",     "M_TROIS"  ],
     [  "M_TRENTE",     "M_QUATRE"  ],
     [  "M_TRENTE",     "M_CINQ"  ],
     [  "M_TRENTE",     "M_SIX"  ],
     [  "M_TRENTE",     "M_SEPT"  ],
     [  "M_TRENTE",     "M_HUIT"  ],
     [  "M_TRENTE",     "M_NEUF"  ],
     [  "M_QUARANTE"  ],
     [  "M_QUARANTE",   "M_ET,"         "M_UN"  ],
     [  "M_QUARANTE",   "M_DEUX"  ],
     [  "M_QUARANTE",   "M_TROIS"  ],
     [  "M_QUARANTE",   "M_QUATRE"  ],
     [  "M_QUARANTE",   "M_CINQ"  ],
     [  "M_QUARANTE",   "M_SIX"  ],
     [  "M_QUARANTE",   "M_SEPT"  ],
     [  "M_QUARANTE",   "M_HUIT"  ],
     [  "M_QUARANTE",   "M_NEUF"  ],
     [  "M_CINQUANTE"  ],
     [  "M_CINQUANTE",  "M_ET,"         "M_UN,"     ],
     [  "M_CINQUANTE",  "M_DEUX"  ],
     [  "M_CINQUANTE",  "M_TROIS"  ],
     [  "M_CINQUANTE",  "M_QUATRE"  ],
     [  "M_CINQUANTE",  "M_CINQ"  ],
     [  "M_CINQUANTE",  "M_SIX"  ],
     [  "M_CINQUANTE",  "M_SEPT"  ],
     [  "M_CINQUANTE",  "M_HUIT"  ],
     [  "M_CINQUANTE",  "M_NEUF"  ],
 ]



dd=datetime.datetime.now()

t = []
t += HEUREs[dd.hour]
t += MINUTEs[dd.minute]
print (t)
for symbol in t:
   print (OUTPUTs[symbol])
