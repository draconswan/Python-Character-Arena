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
    # An image location (where the image is stored in the src package)
    def __init__(self, characterName="", characterClass="", strength=0, quickness=0, armor=0, health=0, imageLoc=""):
        self.characterName = characterName
        self.characterClass = characterClass
        self.strength = strength
        self.quickness = quickness
        self.armor = armor
        self.health = health
        self.wounds = 0
        self.imageLoc = imageLoc
    
    # Returns the stats of each character, minus the unneeded image location
    def __str__(self):
        return "This is the character:\n  Name: %s\n  Class: %s\n  Strength: %d\n  Quickness: %d\n  Armor: %d\n  Max HP: %d\n  Current HP: %d" \
            % (self.characterName, self.characterClass, self.strength, self.quickness, self.armor, self.health, self.getCurrentHP())
    
    # Calculates the current HP (Health Points) a character has by subtracting the amount of damage (wounds) from their HP. Return result
    def getCurrentHP(self):
        currentHP = self.health - self.wounds
        print("    This is %s's current HP: %d" % (self.characterName, currentHP))
        return currentHP
    
    # Calculates an attack roll (roll 1d20, add quickness of attacker) if attackRoll is greater than the defender's
    # armor stat, the defender will take damage. Return result
    def attackRoll(self):
        attackRoll = randint(1, 21) + self.quickness
        print("    This is %s's current attackRoll: %d" % (self.characterName, attackRoll))
        return attackRoll
    
    # Calculates the amount of damage to be dealt to the defender (roll 1d8 damage dice, add strength of attacker). Return result
    def attackDamage(self):
        damage = randint(1, 9) + self.strength
        print("    This is the damage of %s's attack: %d" % (self.characterName, damage))
        return damage
    
    # Adds damage from attacker to the previous damage (wounds) the defender has taken 
    # This method also called the getCurrentHP method which subtracts the amount of damage (wounds) from their HP (Health Points)
    # If the defender is now defeated (HP <= 0), returns True. If the defender is not dead, returns False
    def takeDamage(self, attackDamage):
        self.wounds += attackDamage
        if self.getCurrentHP() <= 0:
            return True
            
        else:
            return False
        
