"""
Created on 4/12/18

@author:   Daniel Swan & Erin Swan
@email:    ds235410@my.stchas.edu
"""

from classes.BattleMessage import BattleMessage


class Arena:
    
    # Each instance of Arena has a player instance of Character, an opponent instance of Character,
    # a current round the battle between the characters is on (global variable initialized to 0)
    # and a static maximum number of rounds (global variable initialized to 5)
    def __init__(self):
        self.player = None
        self.opponent = None
        self.currentRound = 1
        self.maxRounds = 5

    # returns the player and opponent instances of the Character class, the current round and the max rounds of the arena instance
    def __str__(self):
        return "Player: %s\nOpponent: %s\nCurrent Round:%d\nMax Rounds:%d" % (
            self.player, self.opponent, self.currentRound, self.maxRounds)

    # sets the player to the passed-in Character instance of the created or chosen player
    def setPlayer(self, player):
        self.player = player

    # sets the opponent to the passed-in Character instance of the chosen opponent
    def setOpponent(self, opponent):
        self.opponent = opponent

    # Checks to make sure there is a player and an opponent in the current instance of Arena. Returns true or false accordingly
    def isReady(self):
        return ((self.player is not None) and (self.opponent is not None))

    # Resets the wounds (total damage) of the player and opponent to 0 and the current round back to 1
    def resetBattle(self):
        self.player.wounds = 0
        self.opponent.wounds = 0
        self.currentRound = 1

    # Returns the current state of the Arena instance, displayed in the color green in the tkinter window
    def getBattleStatus(self):
        return BattleMessage("Current Round: %d, Player HP: %d, Opponent HP: %d" % (
            self.currentRound, self.player.getCurrentHP(), self.opponent.getCurrentHP()), "green")

    # Evaluates if the battle is over (currentRound > maxRounds) and returns message/exits method if true
    # If the battle is not over, method gets the result of the player attacking the opponent, 
    # storing the numbers and result message of that part of the round
    # and then, if applicable, method gets the result of the opponent attacking the player, 
    # storing the numbers and result message of the second part of the round by adding to the message list msgPrintList
    # increments the current round
    def battleRound(self):
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
            self.currentRound += 1
            return (attackResultTwo[0], msgPrintList)
        else:
            print("Round IS over - player killed opponent - take out")
            self.currentRound += 1
            return attackResultOne

    # Takes in the character instance of the attacker and defender for the specific part of the round
    # creates an empty list for messages to be stored in for later display
    # Calls the attackDamage method from Character class to determine if the attacker was able to
    # hit the defender and, if so, if the defender takes damage. If that is also the case, this method
    # determines if the defender was then defeated by the damage taken.  Each case adds a message to the list msgList
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
