#coding:utf-8

'''
Created on 21 f�vr. 2020

@author: DIALLO Alpha marouana
'''
from OP_Fois import OP_Fois

class OP_Moins:
    '''
    classdocs
    '''


    def __init__(self, suivant):
        '''
        Constructor
        '''
        self._suivant = suivant
    
    def calcul(self, p1, p2, op):
        if op == 1:
            if p1 >= p2:
                return p1 - p2
            else:
                return p2 - p1
        else:
            assert(isinstance(self._suivant, OP_Fois)), "Le suivant est non valide !"
            return self._suivant.calcul(p1, p2, op)