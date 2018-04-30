"""
Created on Apr 11, 2018

@author:   Daniel.Swan
@email:    ds235410@my.stchas.edu
"""
from random import randint

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
    
    def __str__(self):
        return "This is the character:\n  Name: %s\n  Class: %s\n  Strength: %d\n  Quickness: %d\n  Armor: %d\n  Max HP: %d\n  Current HP: %d" \
            % (self.characterName, self.characterClass, self.strength, self.quickness, self.armor, self.health, self.getCurrentHP())
    # Methods needed:
    
    def getCurrentHP(self):
        currentHP = self.health - self.wounds
        print("This is the current HP: %d" % currentHP)
        return currentHP
    
    # attack with weapon (roll a d20, add quickness, return result)
    def weaponAttackRoll(self):
        attackRoll = randint(1, 21) + self.quickness
        print("This is the current attackRoll: %d" % attackRoll)
        return attackRoll
    
    # get weapon damage (roll weapon damage dice, add strength)
    def weaponAttackDamage(self):
        weaponDmg = randint(1, 9) + self.strength
        print("This is the weapon's damage: %d" % weaponDmg)
        return weaponDmg
    
    # get list of weapons
    def getWeapons(self):
        pass
    
    # take damage (add damage to current wounds, return if character is defeated by this damage)
    def takeDamage(self, attackDamage):
        self.wounds += attackDamage
        if self.getCurrentHP() <= 0:
            print("They're dead - take out")
            return True
            
        else:
            print("They're not dead - take out")
            return False
        
