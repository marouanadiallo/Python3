#coding:utf-8

'''
Created on 20 f�vr. 2020

@author:  DIALLO Alpha marouana
'''
import random

class Plaques:
    '''
        une plaque definie un nombre 
    '''

    lesPlaques = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10, 25, 25, 50, 50, 75, 75, 100, 100)
   
    
    @classmethod
    def tirer_plaques(self, nb=6): 
        #return une liste de six nombres (ici des plaques)
        resultat_du_tirage = list()
        i = 0
        while i < nb:
            resultat_du_tirage.append(Plaques.lesPlaques[random.randrange(0,len(Plaques.lesPlaques))])
            i += 1
        return resultat_du_tirage