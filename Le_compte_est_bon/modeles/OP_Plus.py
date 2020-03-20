#coding:utf-8

'''
Created on 21 f�vr. 2020

@author: DIALLO Alpha marouana
'''

class OP_Plus:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def calcul(self, p1, p2, op):
        if op == 0:
            return p1 + p2
        else:
            raise ValueError("ERROR ! Operateur non réconnu")