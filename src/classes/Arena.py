"""
Created on 4/12/18

@author:   Daniel Swan
@email:    ds235410@my.stchas.edu
"""


class Arena:

    def __init__(self):
        self.player = None
        self.opponent = None
        self.currentRound = 0
        self.maxRounds = 10
    
    def setPlayer(self, player):
        self.player = player
    
    def setOpponent(self, opponent):
        self.opponent = opponent
        
    def startBattle(self):
        for index in range(1, self.maxRounds + 1):
            print("Round %d, Fight!" % index)
            self.currentRound = index
            shouldContinue = self.battleRound()
            if shouldContinue:
                pass
            
    def battleRound(self):
        battleOver = self.makeAttack(self.player, self.opponent)
        if not battleOver:
            return self.makeAttack(self.opponent, self.player)
        else:
            return battleOver
    
    def makeAttack(self, attacker, defender):
        attackRoll = attacker.weaponAttackRoll()
        if attackRoll >= defender.armor:
            print("%s's attack hits!" % (attacker.name))
            attackDamage = attacker.weaponAttackDamage()
            stillAlive = defender.takeDamage(attackDamage)
            print("%s takes %d damage." % (defender.name, attackDamage))
            if not stillAlive:
                print("%s is defeated!" % (defender.name))
                return True
            else:
                return False
        else:
            print("%s's attack misses" % (attacker.name))
            return False
