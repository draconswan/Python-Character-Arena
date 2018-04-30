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
        
    def __str__(self):
        print("This is the Arena String")
        return "Player: %s\nOpponent: %s" % (self.player, self.opponent)
    
    def setPlayer(self, player):
        self.player = player
    
    def setOpponent(self, opponent):
        self.opponent = opponent
        
    def startBattle(self):
        for index in range(1, self.maxRounds + 1):
            print("Round %d, Fight!" % index)
            self.currentRound = index
            battleOver = self.battleRound()
            if battleOver:
            #If one is defeated, next steps
                print("Someone is dead - take out")
                return
    
    def getBattleStatus(self):
        print("Current Round: %d, Player HP: %d, Opponent HP: %d" % (self.currentRound, self.player.getCurrentHP(), self.opponent.getCurrentHP()))
            
    def battleRound(self):
        battleOver = self.makeAttack(self.player, self.opponent)
        if not battleOver:
            print("Battle is not over - take out")
            return self.makeAttack(self.opponent, self.player)
        else:
            print("Battle IS over - take out")
            return battleOver
    
    def makeAttack(self, attacker, defender):
        attackRoll = attacker.weaponAttackRoll()
        if attackRoll >= defender.armor:
            print("%s's attack hits!" % (attacker.characterName))
            attackDamage = attacker.weaponAttackDamage()
            isDead = defender.takeDamage(attackDamage)
            print("%s takes %d damage." % (defender.characterName, attackDamage))
            if isDead:
                print("%s is defeated!" % (defender.characterName))
                return True
            else:
                return False
        else:
            print("%s's attack misses" % (attacker.characterName))
            return False
