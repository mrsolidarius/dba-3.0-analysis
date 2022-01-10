# DBA3 Analysis
"""
Analyze probabilities of combat outcomes for each unit type.

@author: captant
@date: 1/6/2022
@originalCreation: 1/3/2022
"""

from DBA3v4 import *
AttackerList = [Elephants(),
           FastKnights(),
           SolidKnights(),
           DoubleKnights(),
           HeavyChariots(),
           Horsemen(),
           DoubleHorsemen(),
           LightChariots(),
           LightHorsemen(),
           CamelRiders(),
           ScythedChariots(),
           Camelry(),
           MountedInfantry(),
           Spears(),
           Spears(hasSideSupport=True),
           DoubleSpears(),
           SolidPikes(),
           SolidPikes(hasRearSupport=True),
           FastPikes(),
           FastPikes(hasRearSupport=True),
           SolidBlades(),
           FastBlades(),
           DoubleFastBlades(),
           SolidAuxilia(),
           FastAuxilia(),
           SolidBows(),
           SolidLongbows(),
           SolidCrossbows(),
           FastBows(),
           FastLongbows(),
           FastCrossbows(),
           DoubleBows(),
           DoubleLongbows(),
           DoubleCrossbows(),
           Psiloi(),
           SolidWarband(),
           FastWarband(),
           SolidHordes(),
           FastHordes()           
        ]

for i in [0,1,2]:
    for j in [0,1,2]:
        x = SolidAuxilia(hasSideSupport=False, numOverlappedBy=i)
        for y in AttackerList:
            y.setNumOverlappedBy(j)
            if y.hasSideSupport == True and y.code == 'Sp':
                print(x.code+';'+
                   y.code+'+'+';'+
                   str(-x.numOverlappedBy)+';'+
                   str(-y.numOverlappedBy)+';'+
                   str(countOutcomes(x,y)))
            elif y.hasRearSupport == True and (y.code == '4Pk' or y.code == '3Pk'):
                print(x.code+';'+
                   y.code+'+'+';'+
                   str(-x.numOverlappedBy)+';'+
                   str(-y.numOverlappedBy)+';'+
                   str(countOutcomes(x,y)))
            else:
                print(x.code+';'+
                   y.code+';'+
                   str(-x.numOverlappedBy)+';'+
                   str(-y.numOverlappedBy)+';'+
                   str(countOutcomes(x,y)))
        



