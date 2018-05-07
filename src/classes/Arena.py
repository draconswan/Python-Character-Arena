"""
Created on 4/12/18

@author:   Daniel Swan & Erin Swan
@email:    ds235410@my.stchas.edu
"""

from classes.BattleMessage import BattleMessage


class Arena:

    def __init__(self):
        self.player = None
        self.opponent = None
        self.currentRound = 0
        self.maxRounds = 5

    def __str__(self):
        return "Player: %s\nOpponent: %s\nCurrent Round:%d\nMax Rounds:%d" % (
            self.player, self.opponent, self.currentRound, self.maxRounds)

    def setPlayer(self, player):
        self.player = player

    def setOpponent(self, opponent):
        self.opponent = opponent

    def startBattle(self):
        for index in range(1, self.maxRounds + 1):
            print("Round %d, Fight!" % index)
            self.currentRound = index
            attackResults = self.battleRound()
            battleOver = attackResults[0]
            if battleOver:
                # If one is defeated, next steps
                battleList = [index, attackResults[1]]
                return battleList

    def isReady(self):
        return ((self.player is not None) and (self.opponent is not None))

    def resetBattle(self):
        self.player.wounds = 0
        self.opponent.wounds = 0
        self.currentRound = 0

    def getBattleStatus(self):
        return BattleMessage("Current Round: %d, Player HP: %d, Opponent HP: %d" % (
            self.currentRound, self.player.getCurrentHP(), self.opponent.getCurrentHP()), "green")

    def battleRound(self):
        self.currentRound += 1
        if self.currentRound > self.maxRounds:
            return (True, [BattleMessage("Battle is over!", "purple")])
        attackResultOne = self.makeAttack(self.player, self.opponent, "blue", "red")
        battleOver = attackResultOne[0]
        msgPrintList = []
        if not battleOver:
            print("Round is not over after player hits; opponent's turn - take out")
            attackResultTwo = self.makeAttack(self.opponent, self.player, "red", "blue")
            msgPrintList += attackResultOne[1]
            msgPrintList += attackResultTwo[1]
            return (attackResultTwo[0], msgPrintList)
        else:
            print("Round IS over - player killed opponent - take out")
            return attackResultOne

    def makeAttack(self, attacker, defender, attackerColor, defenderColor):
        attackRoll = attacker.attackRoll()
        msgList = []
        if attackRoll >= defender.armor:
            attackDamage = attacker.attackDamage()
            isDead = defender.takeDamage(attackDamage)
            attackMessage = BattleMessage("%s's attack hits!" % (attacker.characterName), attackerColor)
            damageMessage = BattleMessage("%s takes %d damage." % (defender.characterName, attackDamage), attackerColor)
            msgList.append(attackMessage)
            msgList.append(damageMessage)
            if isDead:
                isDeadMsg = BattleMessage("%s is defeated!" % (defender.characterName), defenderColor)
                msgList.append(isDeadMsg)
                return (True, msgList)
            else:
                return (False, msgList)

        else:
            attackMessage = BattleMessage("%s's attack misses" % (attacker.characterName), attackerColor)
            msgList.append(attackMessage)
            return (False, msgList)
