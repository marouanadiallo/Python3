#coding:utf-8

'''
Created on 20 fevr. 2020

@author:  DIALLO Alpha marouana
'''

from OP_Fois import OP_Fois
from OP_Plus import OP_Plus
from OP_Moins import OP_Moins
from OP_Division import OP_Division

from Hitorique import Historique

class Joueur:
    '''
    classdocs
    '''


    def __init__(self, pseudo):
        '''
        Constructor
        '''
        self._pseudo = pseudo
        self._score = 0
        
        
        
        
    @property
    def pseudo(self):
        return self._pseudo
    
    @pseudo.setter
    def pseudo(self, pseudo):
        #Verification sur le pseudo pas de caract�re sp�ciaux
        self._pseudo = pseudo
    
    def choisir(self, *choix):
        
        plus = OP_Plus()
        fois = OP_Fois(plus)
        moins = OP_Moins(fois)
        division = OP_Division(moins)
        
        self._operation = [choix[3][choix[0]], choix[1],  choix[3][choix[2]], "=", division.calcul(choix[3][choix[0]], choix[3][choix[2]], choix[1])]
        self.sauvegarge_operation(self._operation)
        
        return division.calcul(choix[3][choix[0]], choix[3][choix[2]], choix[1])
    
    
    #cette methode creer un fichier binaire historique
    def creer_une_historique(self):
        Historique.creer_fichier(self.pseudo)   
    
    def sauvegarge_operation(self, operation):
        Historique.sauvegarde_une_operation(self.pseudo, operation)
        
    def lire_la_sauvegarde(self):
        Historique.lire_le_fichier(self.pseudo)