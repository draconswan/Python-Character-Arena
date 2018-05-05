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
        self.maxRounds = 4
        
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
            attackResults = self.battleRound()
            print(attackResults[1])
            battleOver = attackResults[0]
            if battleOver:
            #If one is defeated, next steps
                battleList = [index, attackResults[1]]
                return battleList
    
    def getBattleStatus(self):
        print("Current Round: %d, Player HP: %d, Opponent HP: %d" % (self.currentRound, self.player.getCurrentHP(), self.opponent.getCurrentHP()))
            
    def battleRound(self):
        attackResultOne = self.makeAttack(self.player, self.opponent)
        battleOver = attackResultOne[0]
        msgPrintList = []
        if not battleOver:
            print("Round is not over after player hits; opponent's turn - take out")
            attackResultTwo = self.makeAttack(self.opponent, self.player)
            msgPrintList.append(attackResultOne[1])
            msgPrintList.append(attackResultTwo[1])
            return (attackResultTwo[0], msgPrintList)
        else:
            print("Round IS over - player killed opponent - take out")
            return attackResultOne
        
    def makeAttack(self, attacker, defender):
        attackRoll = attacker.attackRoll()
        msgList = []
        if attackRoll >= defender.armor:
            attackDamage = attacker.attackDamage()
            isDead = defender.takeDamage(attackDamage)
            attackMessage = "%s's attack hits!\n%s takes %d damage." % (attacker.characterName, defender.characterName, attackDamage)
            msgList.append(attackMessage)
            if isDead:
                isDeadMsg = "%s is defeated!" % (defender.characterName)
                msgList.append(isDeadMsg)
                return (True, msgList)
            else:
                isDeadMsg = "no one is dead - need to take out?"
                msgList.append(isDeadMsg)
                return (False, msgList)
        else:
            attackMessage = "%s's attack misses" % (attacker.characterName)
            isDeadMsg = "nothing right now - replace"
            msgList.append(attackMessage)
            msgList.append(isDeadMsg)
            return (False, msgList)
