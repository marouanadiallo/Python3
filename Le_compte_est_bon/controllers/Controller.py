#coding: utf-8

'''
Created on 29 f�vr. 2020

@author: DIALLO Alpha marouana
'''
from Vue import Vue
from Joueur import Joueur
from Plaque import Plaques

class Controller:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._vue = Vue(self)
        
        
        self._vue.mainloop() #on lance la fenetre
    
    def creer_joueur_mode_entrainement(self, pseudo):
        self._joueur = Joueur(pseudo)
        self._joueur.creer_une_historique()
    
    def tirage(self):
        return Plaques.tirer_6_plaques()  