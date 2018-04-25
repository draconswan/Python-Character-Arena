'''
Created on Apr 11, 2018

@author: es209931
'''

class weapon:
    
    def __init__(self, name = "", damageDie = "1d1"):
        self._name = name
        self._damageDie = damageDie

    # Methods
    # roll damage die (rand in the range of the second d * number of times to roll)
        