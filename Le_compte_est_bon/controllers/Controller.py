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
        
    
    def enregistrer_joueur_et_lancer_entrainement(self, pseudo):
        self._joueur = Joueur(pseudo)
        self._vue.interface_du_entrainement(self.tirage())  #appelle interface d'entrainement
    
    def tirage(self):
        self._list_tirage = Plaques.tirer_plaques()  
        return self._list_tirage
    
    def effectuer_operation(self, indices_plaques, indice_op):
        if len(indices_plaques) != 2  or len(indice_op)!=1 :
            self._vue.lance_alert("Vous devez choisir exactement deux plaques !")
        else:
            self._resultat = self._joueur.effectuer_operation(indices_plaques[0], indice_op[0], indices_plaques[1], self._list_tirage)
            if self._resultat < 0:
                self._vue.lance_alert("L'opération n'est pas valide! NOTE: les nombre négatifs sont proscrit, le reste d'une division non nul est interdit")
            else:
                self.affiche_historique(self._joueur.lire_la_sauvegarde()) #appelle pour l'affiche les operation ajouté
                
                self.supprime_et_ajoute_des_plaque(indices_plaques[0], indices_plaques[1], self._resultat)
                print(self._list_tirage)
                 
                
    def liste_operateur(self):
        return Joueur._op
                    
    def supprimer_derniere_operation(self):
        #supprime la dernière opération éffectuée
        op = self._joueur.supprimer_derniere_operation()    
        
    def affiche_historique(self, sauvegarde):
        self._vue.ajouter_listbox_operation(sauvegarde.index(sauvegarde[len(sauvegarde)-1]), sauvegarde[len(sauvegarde)-1])
    
    def supprime_et_ajoute_des_plaque(self, index1, index2, res):
        print(index1, index2)
        
        del self._list_tirage[index1]
        del self._list_tirage[index2-1] 
        
        self._vue._listbox_des_plaques.delete(index2) #fonction de suppression
        self._vue._listbox_des_plaques.delete(index1)
        
        self._list_tirage.append(res)
        self._vue.ajouter_listbox_plaque(self._list_tirage.index(self._list_tirage[len(self._list_tirage)-1]), self._list_tirage[len(self._list_tirage)-1]) 
        
    def lancer(self):
        self._vue.mainloop() #on lance la fenetre