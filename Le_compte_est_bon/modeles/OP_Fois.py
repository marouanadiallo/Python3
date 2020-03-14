#coding:utf-8

'''
Created on 21 f�vr. 2020

@author: DIALLO Alpha marouana
'''
from OP_Plus import OP_Plus

class OP_Fois:
    '''
    classdocs
    '''


    def __init__(self, suivant):
        '''
        Constructor
        '''
        self._suivant = suivant
    
    def calcul(self, p1, p2, op):
        if op == 2:
            return p1 * p2
        else:
            assert(isinstance(self._suivant, OP_Plus)), "Le suivant est non valide !"
            return self._suivant.calcul(p1, p2, op)