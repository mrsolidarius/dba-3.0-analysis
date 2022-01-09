# DBA3 Analysis
"""
Analyze probabilities of combat outcomes for each unit type.

@author: captant
@date: 1/6/2022
@originalCreation: 1/3/2022
"""

from DBA3v3 import *
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
           DoubleSpears(),
           SolidPikes(),
           FastPikes(),
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

DefenderList = [Elephants(),
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
           DoubleSpears(),
           SolidPikes(),
           FastPikes(),
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

x = Spears(numOverlappedBy=0)
y = Elephants(numOverlappedBy=0)
z = probabilityOutcomes(x,y)
print(x.code+' vs '+y.code+' ('+str(y.numOverlappedBy-x.numOverlappedBy)+')')
print('Win  : '+str(z[0]))
print('Scare: '+str(z[1]))
print('Push : '+str(z[2]))
print('Tie  : '+str(z[3]))
print('Back : '+str(z[4]))
print('Flee : '+str(z[5]))
print('Lose : '+str(z[6]))
print('')

for j in [0,1,2]:
    x = Elephants()
    for i in AttackerList:
        i.setNumOverlappedBy(j)
        print(x.code+';'+
               i.code+';'+
               str(i.numOverlappedBy-x.numOverlappedBy)+';'+
               str(probabilityOutcomes(x,i)))
for j in [1,2]:
    x = Elephants(numOverlappedBy=j)    
    for i in AttackerList:
        i.setNumOverlappedBy(0)
        print(x.code+';'+
               i.code+';'+
               str(i.numOverlappedBy-x.numOverlappedBy)+';'+
               str(probabilityOutcomes(x,i)))
        



