# DBA3 Function Library
"""
Analyze probabilities of combat outcomes for each unit type.

Library of functions to assist.

@author: captant
@date: 1/6/2022
@originalCreation: 1/3/2022
"""

def countOutcomes(Attacker,Defender,combatType='close-combat'):
    CombatOutcomes = CombatOutcomeCounts()
    CombatOutcomes.calculate(Attacker,Defender,combatType)
    outcomeCounts = [CombatOutcomes.numWinDouble,
                     CombatOutcomes.numFlight,
                     CombatOutcomes.numWin,
                     CombatOutcomes.numTie,
                     CombatOutcomes.numLose,
                     CombatOutcomes.numFlee,
                     CombatOutcomes.numLoseDouble]
    return outcomeCounts

def countsToProbabilities(countList):
    total = sum(countList)
    probabilityList = [int(round(100*x/total,0)) for x in countList]
    return probabilityList

def probabilityOutcomes(Attacker,Defender,combatType='close-combat'):
    outcomeCounts = countOutcomes(Attacker,Defender,combatType)
    probabilityCounts = countsToProbabilities(outcomeCounts)
    return probabilityCounts

def vs(Attacker,Defender):
    attackerCombatFactor = Attacker.getCombatFactorVs(Defender)
    defenderCombatFactor = Defender.getCombatFactorVs(Attacker)    
    return attackerCombatFactor, defenderCombatFactor

def shoot(Attacker,Defender):
    attackerCombatFactor = Attacker.getBasicCombatFactorShoot(Defender)
    defenderCombatFactor = Defender.getBasicCombatFactorShoot(Attacker)
    return attackerCombatFactor, defenderCombatFactor

def vsRange(Attacker,Defender):
    attackerVsRange = Attacker.getScoreRangeVs(Defender)
    defenderVsRange = Defender.getScoreRangeVs(Attacker)
    return attackerVsRange, defenderVsRange

def shootRange(Attacker,Defender):
    attackerShootRange = Attacker.getScoreRangeShoot(Defender)
    defenderShootRange = Defender.getScoreRangeShoot(Attacker)
    return attackerShootRange, defenderShootRange

def selectRange(Attacker,Defender,combatType):
    if combatType == 'close-combat':
        attackerRange, defenderRange = vsRange(Attacker,Defender)
    elif combatType == 'shooting':
        attackerRange, defenderRange = shootRange(Attacker,Defender)
    return attackerRange, defenderRange   

class CombatOutcomeCounts(object):
    def __init__(self):
        self.numWinDouble = 0
        self.numFlight = 0
        self.numWin = 0
        self.numTie = 0
        self.numLose = 0
        self.numFlee = 0
        self.numLoseDouble = 0  
        
    def calculate(self,Attacker,Defender,combatType):
        attackerRange, defenderRange = selectRange(Attacker,Defender,combatType)
        for attackerScore in attackerRange:
            for defenderScore in defenderRange:
                Attacker.score = attackerScore
                Defender.score = defenderScore
                self.getResolution(Attacker,Defender)
        return self
    
    def getResolution(self,Attacker,Defender):
        if attackerDoublesDefender(Attacker.score,Defender.score):
            self.applyWinDoubleCase(Attacker,Defender)           
        elif attackerBeatsDefender(Attacker.score,Defender.score):
            self.applyWinCase(Attacker,Defender)           
        elif attackerTiesDefender(Attacker.score,Defender.score):
            self.applyTieCase(Attacker,Defender)          
        elif defenderDoublesAttacker(Attacker.score,Defender.score):
            self.applyLoseDoubleCase(Attacker,Defender)          
        elif defenderBeatsAttacker(Attacker.score,Defender.score):
            self.applyLoseCase(Attacker,Defender)
        return self

    def applyWinDoubleCase(self,Attacker,Defender):
        self.forCavalryWinDouble(Attacker,Defender)
        self.forLightHorseWinDouble(Attacker,Defender)
        self.forPsiloiAndOthersWinDouble(Attacker,Defender)
        return self
    
    def applyWinCase(self,Attacker,Defender):
        self.forElephantsWin(Attacker,Defender)
        self.forScythedChariotsWin(Attacker,Defender)
        self.forKnightsWin(Attacker,Defender)
        self.forCamelryWin(Attacker,Defender)
        self.forCavalryWin(Attacker,Defender)
        self.forLightHorseWin(Attacker,Defender)
        self.forSpearsPikesBladesWin(Attacker,Defender)
        self.forAuxiliaWin(Attacker,Defender)
        self.forBowsWin(Attacker,Defender)
        self.forPsiloiWin(Attacker,Defender)
        self.forWarbandWin(Attacker,Defender)
        self.forHordesWin(Attacker,Defender)
        self.forWarWagonsWin(Attacker,Defender)
        self.forArtilleryWin(Attacker,Defender)
        return self
    
    def applyTieCase(self,Attacker,Defender):
        self.forScythedChariotsTie(Attacker,Defender)
        self.forKnightsCamelryTie(Attacker,Defender)
        self.forOtherMountedTie(Attacker,Defender)
        self.forFastFootAndOthersTie(Attacker,Defender)
        return self
    
    def applyLoseCase(self,Attacker,Defender):
        self.forElephantsLose(Attacker,Defender)
        self.forScythedChariotsLose(Attacker,Defender)
        self.forKnightsLose(Attacker,Defender)
        self.forCamelryLose(Attacker,Defender)
        self.forCavalryLose(Attacker,Defender)
        self.forLightHorseLose(Attacker,Defender)
        self.forSpearsPikesBladesLose(Attacker,Defender)
        self.forAuxiliaLose(Attacker,Defender)
        self.forBowsLose(Attacker,Defender)
        self.forPsiloiLose(Attacker,Defender)
        self.forWarbandLose(Attacker,Defender)
        self.forHordesLose(Attacker,Defender)
        self.forWarWagonsLose(Attacker,Defender)
        self.forArtilleryLose(Attacker,Defender)
        return self
    
    def applyLoseDoubleCase(self,Attacker,Defender):
        self.forCavalryLoseDouble(Attacker,Defender)
        self.forLightHorseLoseDouble(Attacker,Defender)
        self.forPsiloiAndOthersLoseDouble(Attacker,Defender)
        return self

    def forArtilleryWin(self,Attacker,Defender):
        if Defender.type == 'ARTILLERY':
            self.numWinDouble += 1
        return self
    
    def forWarWagonsWin(self,Attacker,Defender):
        if Defender.type == 'WAR WAGON':
            if Attacker.type == 'ELEPHANTS':
                self.numWinDouble += 1
            else:
                self.numTie += 1
        return self
    
    def forHordesWin(self,Attacker,Defender):
        if Defender.type == 'HORDES':
            if Defender.terrain == 'good-going' and (Attacker.type == 'KNIGHTS' or Attacker.type == 'ELEPHANTS'):
                self.numWinDouble += 1
            elif Attacker.type == 'WARBAND':
                self.numWinDouble += 1
            else:
                self.numTie += 1
        return self
    
    def forWarbandWin(self,Attacker,Defender):
        if Defender.type == 'WARBAND':
            if Defender.terrain == 'good-going' and (Attacker.type == 'KNIGHTS' or Attacker.type == 'SCYTHED CHARIOTS'):
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forPsiloiWin(self,Attacker,Defender):
        if Defender.type == 'PSILOI':
            if Attacker.terrain == 'good-going' and (Attacker.type == 'KNIGHTS' or Attacker.type == 'CAVALRY' or Attacker.type == 'CAMELRY'):
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forBowsWin(self,Attacker,Defender):
        if Defender.type == 'BOWS':
            if Attacker.style == 'mounted':
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forAuxiliaWin(self,Attacker,Defender):
        if Defender.type == 'AUXILIA':
            if Defender.terrain == 'good-going' and Attacker.type == 'KNIGHTS':
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forSpearsPikesBladesWin(self,Attacker,Defender):
        if Defender.type == 'SPEARS' or Defender.type == 'PIKES' or Defender.type == 'BLADES':
            if Defender.terrain == 'good-going' and (Attacker.type == 'KNIGHTS' or Attacker.type == 'SCYTHED CHARIOTS'):
                self.numWinDouble += 1
            elif Attacker.type == 'WARBAND':
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forLightHorseWin(self,Attacker,Defender):
        if Defender.type == 'LIGHT HORSE':
            if Defender.terrain == 'bad-going':
                self.numFlight += 1
            elif Attacker.type == 'SCYTHED CHARIOTS':
                self.numFlight += 1
            else:
                self.numWin += 1
        return self
    
    def forCavalryWin(self,Attacker,Defender):
        if Defender.type == 'CAVALRY':
            if Defender.terrain == 'bad-going':
                self.numFlight += 1
            elif Attacker.type == 'SCYTHED CHARIOTS':
                self.numFlight += 1
            else:
                self.numWin += 1
        return self
    
    def forCamelryWin(self,Attacker,Defender):
        if Defender.type == 'CAMELRY':
            if Defender.terrain == 'bad-going':
                self.numWinDouble += 1
            elif Attacker.type == 'SCYTHED CHARIOTS':
                self.numWinDouble += 1
            elif Attacker.type == 'ELEPHANTS':
                self.numFlight += 1
            else:
                self.numWin += 1
        return self
    
    def forKnightsWin(self,Attacker,Defender):
        if Defender.type == 'KNIGHTS':
            if Attacker.type == 'ELEPHANTS' or Attacker.type == 'SCYTHED CHARIOTS' or Attacker.type == 'CAMELRY' or Attacker.type == 'LIGHT HORSE':
                self.numWinDouble += 1
            else:
                self.numWin += 1
        return self
    
    def forScythedChariotsWin(self,Attacker,Defender):
        if Defender.type == 'SCYTHED CHARIOTS':
            self.numWinDouble += 1
        return self
    
    def forElephantsWin(self,Attacker,Defender):
        if Defender.type == 'ELEPHANTS':
            if Attacker.type == 'PSILOI' or Attacker.type == 'AUXILIA' or Attacker.type == 'LIGHT HORSE':
                self.numWinDouble += 1
            elif Attacker.type == 'ARTILLERY':
                self.numWinDouble += 1
            elif Attacker.type == 'ELEPHANTS':
                self.numFlight += 1
            else:
                self.numWin += 1
        return self
    
    def forArtilleryLose(self,Attacker,Defender):
        if Attacker.type == 'ARTILLERY':
            self.numLoseDouble += 1
        return self
    
    def forWarWagonsLose(self,Attacker,Defender):
        if Attacker.type == 'WAR WAGON':
            if Defender.type == 'ELEPHANTS':
                self.numLoseDouble += 1
            else:
                self.numTie += 1
        return self
    
    def forHordesLose(self,Attacker,Defender):
        if Attacker.type == 'HORDES':
            if Attacker.terrain == 'good-going' and (Defender.type == 'KNIGHTS' or Defender.type == 'ELEPHANTS'):
                self.numLoseDouble += 1
            elif Defender.type == 'WARBAND':
                self.numLoseDouble += 1
            else:
                self.numTie += 1
        return self
    
    def forWarbandLose(self,Attacker,Defender):
        if Attacker.type == 'WARBAND':
            if Attacker.terrain == 'good-going' and (Defender.type == 'KNIGHTS' or Defender.type == 'SCYTHED CHARIOTS'):
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forPsiloiLose(self,Attacker,Defender):
        if Attacker.type == 'PSILOI':
            if Defender.terrain == 'good-going' and (Defender.type == 'KNIGHTS' or Defender.type == 'CAVALRY' or Defender.type == 'CAMELRY'):
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forBowsLose(self,Attacker,Defender):
        if Attacker.type == 'BOWS':
            if Defender.style == 'mounted':
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forAuxiliaLose(self,Attacker,Defender):
        if Attacker.type == 'AUXILIA':
            if Attacker.terrain == 'good-going' and Defender.type == 'KNIGHTS':
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forSpearsPikesBladesLose(self,Attacker,Defender):
        if Attacker.type == 'SPEARS' or Attacker.type == 'PIKES' or Attacker.type == 'BLADES':
            if Attacker.terrain == 'good-going' and (Defender.type == 'KNIGHTS' or Defender.type == 'SCYTHED CHARIOTS'):
                self.numLoseDouble += 1
            elif Defender.type == 'WARBAND':
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forLightHorseLose(self,Attacker,Defender):
        if Attacker.type == 'LIGHT HORSE':
            if Attacker.terrain == 'bad-going':
                self.numFlee += 1
            elif Defender.type == 'SCYTHED CHARIOTS':
                self.numFlee += 1
            else:
                self.numLose += 1
        return self
    
    def forCavalryLose(self,Attacker,Defender):
        if Attacker.type == 'CAVALRY':
            if Attacker.terrain == 'bad-going':
                self.numFlee += 1
            elif Defender.type == 'SCYTHED CHARIOTS':
                self.numFlee += 1
            else:
                self.numLose += 1
        return self
    
    def forCamelryLose(self,Attacker,Defender):
        if Attacker.type == 'CAMELRY':
            if Attacker.terrain == 'bad-going':
                self.numLoseDouble += 1
            elif Defender.type == 'SCYTHED CHARIOTS':
                self.numLoseDouble += 1
            elif Defender.type == 'ELEPHANTS':
                self.numFlee += 1
            else:
                self.numLose += 1
        return self
    
    def forKnightsLose(self,Attacker,Defender):
        if Attacker.type == 'KNIGHTS':
            if Defender.type == 'ELEPHANTS' or Defender.type == 'SCYTHED CHARIOTS' or Defender.type == 'CAMELRY' or Defender.type == 'LIGHT HORSE':
                self.numLoseDouble += 1
            else:
                self.numLose += 1
        return self
    
    def forScythedChariotsLose(self,Attacker,Defender):
        if Attacker.type == 'SCYTHED CHARIOTS':
            self.numLoseDouble += 1
        return self
    
    def forElephantsLose(self,Attacker,Defender):
        if Attacker.type == 'ELEPHANTS':
            if Defender.type == 'PSILOI' or Defender.type == 'AUXILIA' or Defender.type == 'LIGHT HORSE':
                self.numLoseDouble += 1
            elif Defender.type == 'ARTILLERY':
                self.numLoseDouble += 1
            elif Defender.type == 'ELEPHANTS':
                self.numFlee += 1
            else:
                self.numLose += 1
        return self
    
        
    def forCavalryWinDouble(self,Attacker,Defender):
        if Defender.type == 'CAVALRY':
            if Attacker.type == 'PIKES' or Attacker.type == 'SPEARS'  or Attacker.type == 'HORDES':
                if Defender.terrain == 'good-going':
                    self.numFlight += 1
            elif Attacker.type == 'ARTILLERY':
                    self.numFlight += 1
            else:
                    self.numWinDouble += 1
        return self
    
    def forLightHorseWinDouble(self,Attacker,Defender):
        if Defender.type == 'LIGHT HORSE':
            if Defender.terrain == 'bad-going':
                self.numWinDouble += 1
            elif Attacker.style == 'mounted':
                self.numWinDouble += 1
            elif Attacker.type == 'BOWS' or Attacker.type == 'PSILOI':
                self.numWinDouble += 1
            else:
                self.numFlight += 1
        return self
    
    def forPsiloiAndOthersWinDouble(self,Attacker,Defender):
        if Defender.type == 'PSILOI':
            if Attacker.type == 'KNIGHTS' or Attacker.type == 'CAVALRY' or Attacker.type == 'CAMELRY' or Defender.type == 'LIGHT HORSE':
                if Attacker.terrain == 'good-going':
                    self.numWinDouble += 1
            elif Attacker.type == 'AUXILIA' or Attacker.type == 'BOWS' or Attacker.type == 'PSILOI':
                self.numWinDouble += 1
            elif Attacker.type == 'ELEPHANTS' or Attacker.type == 'SCYTHED CHARIOTS':
                self.numWin += 1
            else:
                self.numFlight += 1
        else:
            self.numWinDouble += 1
        return self
    
    def forCavalryLoseDouble(self,Attacker,Defender):
        if Attacker.type == 'CAVALRY':
            if Defender.type == 'PIKES' or Defender.type == 'SPEARS'  or Defender.type == 'HORDES':
                if Attacker.terrain == 'good-going':
                    self.numFlee += 1
            elif Defender.type == 'ARTILLERY':
                    self.numFlee += 1
            else:
                    self.numLoseDouble += 1
        return self
    
    def forLightHorseLoseDouble(self,Attacker,Defender):
        if Attacker.type == 'LIGHT HORSE':
            if Attacker.terrain == 'bad-going':
                self.numLoseDouble += 1
            elif Defender.style == 'mounted':
                self.numLoseDouble += 1
            elif Defender.type == 'BOWS' or Defender.type == 'PSILOI':
                self.numLoseDouble += 1
            else:
                self.numFlee += 1
        return self
    
    def forPsiloiAndOthersLoseDouble(self,Attacker,Defender):
        if Attacker.type == 'PSILOI':
            if Defender.type == 'KNIGHTS' or Defender.type == 'CAVALRY' or Defender.type == 'CAMELRY' or Defender.type == 'LIGHT HORSE':
                if Defender.terrain == 'good-going':
                    self.numLoseDouble += 1
            elif Defender.type == 'AUXILIA' or Defender.type == 'BOWS' or Defender.type == 'PSILOI':
                self.numLoseDouble += 1
            elif Defender.type == 'ELEPHANTS' or Defender.type == 'SCYTHED CHARIOTS':
                self.numLose += 1
            else:
                self.numFlee += 1
        else:
            self.numLoseDouble += 1
        return self
            
    def forScythedChariotsTie(self,Attacker,Defender):
        if Attacker.type == 'SCYTHED CHARIOTS':
            self.numLoseDouble += 1
        elif Defender.type == 'SCYTHED CHARIOTS':
            self.numWinDouble += 1
        return self
    
    def forKnightsCamelryTie(self,Attacker,Defender):
        if Attacker.type == 'KNIGHTS' or Attacker.type == 'CAMELRY':
            if Defender.type == 'BLADES' or Defender.code.find('Lb') > -1 or Defender.code.find('Cb') > -1:
                self.numLoseDouble += 1
            elif Defender.style == 'foot' and Defender.classification == 'Solid':
                self.numLose += 1
        elif Defender.type == 'KNIGHTS' or Defender.type == 'CAMELRY':
            if Attacker.type == 'BLADES' or Attacker.code.find('Lb') > -1 or Attacker.code.find('Cb') > -1:
                self.numWinDouble += 1
            elif Attacker.style == 'foot' and Attacker.classification == 'Solid':
                self.numWin += 1       
        if Attacker.code == '4Kn' and Defender.code == '3Kn':
            self.numLose += 1
        elif Defender.code == '4Kn' and Attacker.code == '3Kn':
            self.numWin += 1
        return self
    
    def forOtherMountedTie(self,Attacker,Defender):
        if Attacker.style == 'mounted' and Attacker.type != 'KNIGHTS' and Attacker.type != 'CAMELRY':
            if Defender.style == 'foot' and Defender.classification == 'Solid':
                self.numLose += 1
        elif Defender.style == 'mounted' and Defender.type != 'KNIGHTS' and Defender.type != 'CAMELRY':
            if Attacker.style == 'foot' and Attacker.classification == 'Solid':
                self.numWin += 1
        return self
    
    def forFastFootAndOthersTie(self,Attacker,Defender):
        if Attacker.style == 'foot' and Attacker.classification == 'Fast':
            if Defender.style == 'foot' and Defender.classification == 'Solid':
                self.numLose += 1
        elif Defender.style == 'foot' and Defender.classification == 'Fast':
            if Attacker.style == 'foot' and Attacker.classification == 'Solid':
                self.numWin += 1
        else:
            self.numTie += 1
        return self     
    

class Units(object):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        self.terrain = terrain
        self.position = position
        self.hasRearSupport = hasRearSupport
        self.hasSideSupport = hasSideSupport
        self.numOverlappedBy = numOverlappedBy
        self.score = None
    
    def setNumOverlappedBy(self,numOverlappedBy):
        self.numOverlappedBy = numOverlappedBy
    
    def getScoreRangeVs(self,Enemy):
        combatFactor = self.getCombatFactorVs(Enemy)
        low = max(1+combatFactor,0)
        high = max(1+6+combatFactor,0)
        scoreRange = range(low,high)
        return scoreRange
    
    def getScoreRangeShoot(self,Enemy):
        combatFactor = self.getBasicCombatFactorShoot(Enemy)
        low = max(1+combatFactor,0)
        high = max(1+6+combatFactor,0)
        scoreRange = range(low,high)
        return scoreRange
    
    def getCombatFactorVs(self,Enemy):
        basicCombatFactor = self.getBasicCombatFactorVs(Enemy)
        supportFactor = self.getSupportFactorVs(Enemy)
        tacticalFactor = self.getTacticalFactorVs()
        combatFactor = basicCombatFactor + supportFactor + tacticalFactor
        return combatFactor
    
    def getBasicCombatFactorVs(self,Enemy):
        enemyStyle = Enemy.style
        if enemyStyle == 'foot':
            combatFactor = self.vsFoot
        elif enemyStyle == 'mounted':
            combatFactor = self.vsMounted
        return combatFactor
    
    def getSupportFactorVs(self,Enemy):
        if self.terrain == 'good-going':
            rearSupport = self.getRearSupportFactorVs(Enemy)
            flankSupport = self.getFlankSupportFactorVs(Enemy)
        else:
            rearSupport = 0
            flankSupport = 0
        support = rearSupport + flankSupport
        return support
    
    def getTacticalFactorVs(self):
        tactical = -1*self.numOverlappedBy
        return tactical
    
    def getRearSupportFactorVs(self,Enemy):
        if self.hasRearSupport:
            if self.type == 'PIKES':
                if Enemy.style == 'foot' and Enemy.type != 'PSILOI':
                    rearSupport = 3
                elif Enemy.type == 'KNIGHTS' or Enemy.type == 'ELEPHANTS' or Enemy.type == 'SCYTHED CHARIOTS':
                    rearSupport = 1
            elif self.type == 'WARBAND' and Enemy.style == 'foot' and Enemy.type != 'PSILOI':
                rearSupport = 1
            elif self.type == 'LIGHT HORSE':
                rearSupport = 1
            else:
                rearSupport = 0
        else:
            rearSupport = 0
        return rearSupport
    
    def getFlankSupportFactorVs(self,Enemy):
        if self.hasSideSupport:
            if self.type == 'SPEARS':
                flankSupport = 1
            elif self.type == 'BOWS' and self.classification == 'Solid':
                flankSupport = 1
            else:
                flankSupport = 0
        else:
            flankSupport = 0
        return flankSupport
    
    def getBasicCombatFactorShoot(self,Enemy):
        enemyStyle = Enemy.style
        if enemyStyle == 'foot':
            combatFactor = self.shootFoot
        elif enemyStyle == 'mounted':
            combatFactor = self.shootMounted
        return combatFactor

class Mounted(Units):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Units.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.style = 'mounted'
        
class Foot(Units):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Units.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.style = 'foot'
        
class Elephants(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'ELEPHANTS'
        self.code = 'El'
        self.vsFoot = 5
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
        
class Knights(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'KNIGHTS'
        self.vsFoot = 3
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class FastKnights(Knights):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Knights.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Kn' 
class SolidKnights(Knights):
      def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Knights.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Kn'              
class DoubleKnights(Knights):
      def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Knights.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '6Kn'         
class HeavyChariots(Knights):
      def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Knights.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'HCh'
        
class Cavalry(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'CAVALRY'
        self.vsFoot = 3
        self.vsMounted = 3
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class Horsemen(Cavalry):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Cavalry.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'Cv'        
class DoubleHorsemen(Cavalry):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Cavalry.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '6Cv'        
class LightChariots(Cavalry):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Cavalry.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'LCh'
        
class LightHorse(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'LIGHT HORSE'
        self.vsFoot = 2
        self.vsMounted = 2   
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class LightHorsemen(LightHorse):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        LightHorse.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'LH'        
class CamelRiders(LightHorse):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        LightHorse.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'LCm'
        
class ScythedChariots(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'SCYTHED CHARIOTS'
        self.code = 'SCh'
        self.vsFoot = 3
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
        
class Camelry(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'CAMELRY'
        self.code = 'Cm'
        self.vsFoot = 3
        self.vsMounted = 3
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
        
class MountedInfantry(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'MOUNTED INFANTRY'
        self.code = 'Mtd-X'
        self.vsFoot = 3
        self.vsMounted = 3
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted

class Spearmen(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'SPEARS'
        self.classification = 'Solid'
        self.vsFoot = 4
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class Spears(Spearmen):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Spearmen.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'Sp'
class DoubleSpears(Spearmen):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Spearmen.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '8Sp'
        
class Pikes(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport,hasSideSupport)
        self.type = 'PIKES'
        self.vsFoot = 3
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class SolidPikes(Pikes):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Pikes.__init__(self,terrain,position,hasRearSupport,hasSideSupport)
        self.code = '4Pk'
        self.classification = 'Solid'
class FastPikes(Pikes):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Pikes.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Pk'
        self.classification = 'Fast'
        
class Blades(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'BLADES'
        self.vsFoot = 5
        self.vsMounted = 3
        self.shootFoot = 4
        self.shootMounted = self.vsMounted
class SolidBlades(Blades):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Blades.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Bd'  
        self.classification = 'Solid'
class FastBlades(Blades):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Blades.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Bd'
        self.classification = 'Fast'
class DoubleFastBlades(Blades):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Blades.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '6Bd'
        self.classification = 'Fast'
        
class Auxilia(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'AUXILIA'
        self.vsFoot = 3
        self.vsMounted = 3
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class SolidAuxilia(Auxilia):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Auxilia.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Ax'
        self.classification = 'Solid'
class FastAuxilia(Auxilia):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Auxilia.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Ax'
        self.classification = 'Fast'
        
class Bows(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'BOWS'
        self.vsFoot = 2
        self.vsMounted = 4
        self.shotAt = 2
        self.shootFoot = 2
        self.shootMounted = 4
class SolidBows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Bw'
        self.classification = 'Solid'
class SolidLongbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Lb'
        self.classification = 'Solid'
class SolidCrossbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Cb'
        self.classification = 'Solid'
class FastBows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Bw'
        self.classification = 'Fast'
class FastLongbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Lb'
        self.classification = 'Fast'
class FastCrossbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Cb'
        self.classification = 'Fast'
class DoubleBows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '8Bw'
        self.classification = 'Solid'
class DoubleLongbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '8Lb'
        self.classification = 'Solid'
class DoubleCrossbows(Bows):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Bows.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '8Cb'
        self.classification = 'Solid'
        
class Psiloi(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'PSILOI'
        self.code = 'Ps'
        self.classification = 'Fast'
        self.vsFoot = 2
        self.vsMounted = 2
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
        
class Warband(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'WARBAND'
        self.vsFoot = 3
        self.vsMounted = 2
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class SolidWarband(Warband):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Warband.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '4Wb'
        self.classification = 'Solid'
class FastWarband(Warband):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Warband.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '3Wb'
        self.classification = 'Fast'
        
class Hordes(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'HORDES'
        self.vsFoot = 3
        self.vsMounted = 2
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class SolidHordes(Hordes):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Hordes.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '7Hd'
        self.classification = 'Solid'
class FastHordes(Hordes):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Hordes.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = '5Hd'
        self.classification = 'Fast'
        
class Artillery(Foot):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Foot.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'ARTILLERY'
        self.code = 'Art'
        self.vsFoot = 4
        self.vsMounted = 4
        self.shotAt = 4
        self.shootFoot = 4
        self.shootMounted = 4
        
class WarWagons(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'WAR WAGONS'
        self.code = 'WWg'
        self.vsFoot = 3
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
        
class General(Mounted):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        Mounted.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.type = 'GENERAL'
        self.vsFoot = 3
        self.vsMounted = 4
        self.shootFoot = self.vsFoot
        self.shootMounted = self.vsMounted
class CommandPoint(General):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        General.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'CP'
class Litter(General):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        General.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'Lit'
class CommandWagon(General):
    def __init__(self,terrain='good-going',position=(0,0),
                 hasRearSupport=False, hasSideSupport=False, numOverlappedBy=0):
        General.__init__(self,terrain,position,hasRearSupport, hasSideSupport, numOverlappedBy)
        self.code = 'CWg'
    
def makeLowercase(inputString):
    string = inputString.lower()
    return string

def attackerDoublesDefender(attackerScore,defenderScore):
    doublesDefender = (attackerScore >= 2*defenderScore)
    return doublesDefender

def attackerBeatsDefender(attackerScore,defenderScore):
    beatsDefender = (attackerScore > defenderScore)
    return beatsDefender

def attackerTiesDefender(attackerScore,defenderScore):
    tiesDefender = (attackerScore == defenderScore)
    return tiesDefender

def defenderDoublesAttacker(attackerScore,defenderScore):
    doublesAttacker = (2*attackerScore <= defenderScore)
    return doublesAttacker

def defenderBeatsAttacker(attackerScore,defenderScore):
    beatsAttacker = (attackerScore < defenderScore)
    return beatsAttacker 