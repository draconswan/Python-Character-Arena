"""
Created on Apr 11, 2018

@author:   Daniel.Swan
@email:    ds235410@my.stchas.edu
"""


# This class contains all of the information needed to build and use both players and opponents
class Character:

    # Characters have:
    # A name
    # A class (for flavor only at this point)
    # A strength (the amount of damage added to each hit)
    # A quickness (the amount added to each attack roll)
    # An armor (the number attacks rolls need to meet or beat to hit)
    # A health score (the amount of damage a character can take before they are defeated)
    def __init__(self, characterName="", characterClass="", strength=0, quickness=0, armor=0, health=0):
        self.characterName = characterName
        self.characterClass = characterClass
        self.strength = strength
        self.quickness = quickness
        self.armor = armor
        self.health = health
        self.wounds = 0
        self.weapons = []

    # Methods needed:
    # get current HP (health - wounds)
    # attack with weapon (roll a d20, add quickness, return result)
    def weaponAttackRoll(self):
        pass
    # get weapon damage (roll weapon damage dice, add strength)
    def weaponAttackDamage(self):
        pass
    # get list of weapons
    # take damage (add damage to current wounds, return if character is defeated by this damage)
    def takeDamage(self, attackDamage):
        pass
