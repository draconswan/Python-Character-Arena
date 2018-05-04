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
        self.maxRounds = 1
        
    def __str__(self):
        print("This is the Arena String")
        return "Player: %s\nOpponent: %s" % (self.player, self.opponent)
    
    def setPlayer(self, player):
        self.player = player
    
    def setOpponent(self, opponent):
        self.opponent = opponent
        
    def startBattle(self):
        battleList = []
        for index in range(1, self.maxRounds + 1):
            print("Round %d, Fight!" % index)
            self.currentRound = index
            battleOver = self.battleRound()
            battleOverTF = battleOver[0]
            attackMessage = battleOver[1]
            isDeadMsg = battleOver[2]
            if battleOverTF:
            #If one is defeated, next steps
                battleList = [index, attackMessage, isDeadMsg]
                return battleList
    
    def getBattleStatus(self):
        print("Current Round: %d, Player HP: %d, Opponent HP: %d" % (self.currentRound, self.player.getCurrentHP(), self.opponent.getCurrentHP()))
            
    def battleRound(self):
        battleOver = self.makeAttack(self.player, self.opponent)
        battleOverTF = battleOver[0]
        if not battleOverTF:
            print("Battle is not over - take out")
            return self.makeAttack(self.opponent, self.player)
        else:
            print("Battle IS over - take out")
            return battleOver
    
    def makeAttack(self, attacker, defender):
        attackRoll = attacker.weaponAttackRoll()
        if attackRoll >= defender.armor:
            attackDamage = attacker.weaponAttackDamage()
            isDead = defender.takeDamage(attackDamage)
            attackMessage = "%s's attack hits!\n%s takes %d damage." % (attacker.characterName, defender.characterName, attackDamage)
            if isDead:
                isDeadMsg = "%s is defeated!" % (defender.characterName)
                return (True, attackMessage, isDeadMsg)
            else:
                isDeadMsg = "no one is dead - need to take out?"
                return (False, attackMessage, isDeadMsg)
        else:
            attackMessage = "%s's attack misses" % (attacker.characterName)
            isDeadMsg = "nothing right now - replace"
            return (False, attackMessage, isDeadMsg)
