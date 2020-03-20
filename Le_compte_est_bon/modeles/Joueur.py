#coding:utf-8

'''
Created on 20 fevr. 2020

@author:  DIALLO Alpha marouana
'''

from OP_Fois import OP_Fois
from OP_Plus import OP_Plus
from OP_Moins import OP_Moins
from OP_Division import OP_Division


class Joueur:
    '''
    classdocs
    '''

    _op=("+","-","*","/")
    def __init__(self, pseudo):
        '''
        Constructor
        '''
        self._pseudo = pseudo
        self._score = 0
        self._list_operations = list()
        
        
        
        
    @property
    def pseudo(self):
        return self._pseudo
    
    @pseudo.setter
    def pseudo(self, pseudo):
        #Verification sur le pseudo pas de caract�re sp�ciaux
        self._pseudo = pseudo
    
    def effectuer_operation(self, *choix):
        """
            Elle attend quatre paramètre cette fonction,
            l'indice de la première plaque => choix[0]
            l'indice de l'operateur choisie => choix[1]
            l'indice de la seconde plaque => choix[2]
            et enfin la liste des six plaque qui on été tirée au hazard 
        """ 
        #Une chaine de responsabilité sur les opérateurs possible
        plus = OP_Plus()
        fois = OP_Fois(plus)
        moins = OP_Moins(fois)
        division = OP_Division(moins)
        
        resultat = division.calcul(choix[3][choix[0]], choix[3][choix[2]], choix[1])
        if resultat < 0 :
            return -1
        
        operation = [choix[3][choix[0]], Joueur._op[choix[1]],  choix[3][choix[2]], "=", resultat]
        self.sauvegarge_operation(operation)
        
        return resultat
    
    def sauvegarge_operation(self, operation):
        self._list_operations.append(operation)
        
    def lire_la_sauvegarde(self):
        return self._list_operations
    
    def supprimer_derniere_operation(self):
        return self._list_operations.pop()