#coding:utf-8

'''
Created on 21 f�vr. 2020

@author: DIALLO Alpha marouana
'''
from OP_Moins import OP_Moins

class OP_Division:
    '''
    classdocs
    '''


    def __init__(self, suivant):
        '''
        Constructor
        '''
        self._suivant = suivant
        
    
    def calcul(self, p1, p2, op):
        if op == 3:
            if (p1 / p2 != 0 ):
                return "ERROR! La première plaque doit être divisible par la seconde !"
            else:
                return p1 * p2
        else:
            assert(isinstance(self._suivant, OP_Moins)), "Le suivant est non valide !"
            return self._suivant.calcul(p1,p2, op)
            