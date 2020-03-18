#coding:utf-8

'''
Created on 20 f�vr. 2020

@author: X
'''
import pickle
import os

class Historique:
    '''
    classdocs
    '''

    _path = "Historique_Joueurs/"
    
    @classmethod
    def creer_fichier(self, nom_du_fichier):
        fichier = open("{}{}.data".format(Historique._path, nom_du_fichier), "ab") 
        fichier.close()
    
    @classmethod
    def lire_le_fichier(self,nom_du_fichier):
        #Cette methode lit un fichier du joueur courant et affiche le contenu
        #sinon affiche que l'historique est vide, aucune operation n'a été effectuée
        
        if Historique.fichier_exist_et_non_vider("{}{}.data".format(Historique._path, nom_du_fichier)):
            
            with open("{}{}.data".format(Historique._path, self._nom_du_fichier), "rb") as fichier_en_lecture:
                lecture = pickle.Unpickler(fichier_en_lecture)
                self._contenu = lecture.load()
            return self._contenu
        else:
            return "Votre historique est vide, veuillez effectuer une opération !"
    
    @classmethod
    def sauvegarde_une_operation(self, nom_du_fichier, operation):
        #cette methode prend en paramètre liste qui est composée de : [operandeGauche, operateur, operandeDroite, le_resultat]
        #Et sauvegarde par ligne une operation
        
        with open("{}{}.data".format(Historique._path, nom_du_fichier), "ab") as fichier_ecriture:
            ecriture = pickle.Pickler(fichier_ecriture)
            ecriture.dump(operation)
            
     
    @classmethod       
    def fichier_exist_et_non_vide(self, fpath):  
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
    
    @classmethod
    def supprimer_une_ligne(self, position):
        #Cette methode s'occupe de la suppression d'une historique
        pass
        