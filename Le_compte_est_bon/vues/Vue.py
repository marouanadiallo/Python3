#coding:utf-8

'''
Created on 29 f�vr. 2020

@author: Alpha marouana DIALLO
'''
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import MULTIPLE, EXTENDED, LEFT, BOTTOM
from idlelib import sidebar
from cgitb import text

from Constants import *
from Accueil import *
from Button import Button
class Vue(tk.Tk):
    '''
        
    '''

    taille_fenetre = (720,480)
    
    def __init__(self, controller):
        '''
        Constructor
        '''
        tk.Tk.__init__(self)
        
        #Définition du titre, fond, logo de la fenetre principale
        self.title(le_titre)
        self.iconbitmap(le_path_logo)
        self.config(bg = la_couleur_du_fond)
        
        self._controller = controller #instance du controller
        
        #appel de quelques methodes qui definissent les propriétés de la fenetre principale
        self.taille_de_la_fenetre()     #On fixe la taille
        self.accueil()                  #Le text d'accueil et le bouton lancé une partie
    
    def taille_de_la_fenetre(self):
        self.geometry(f"{Vue.taille_fenetre[0]}x{Vue.taille_fenetre[1]}")
        self.resizable(width = False, height = False)
        
    def accueil(self):
        """
            cette methode invoque deux methode du module Accueil
        """
        self._cadre_accueil = tk.Frame(self, bg = la_couleur_du_fond)
        
        les_labels_accueil(self._cadre_accueil, tk) 
        les_button_accueil(self._cadre_accueil, self.formulaire_creation_joueur)
        self._cadre_accueil.pack(expand="yes")
        """
        #Ajouter du text d'accueil
        self._text_accueil = tk.Label(self._cadre_accueil, text="Bienvenue sur le jeu de Maths", font=("Courrier", 25), bg = la_couleur_du_fond, fg="white").pack()
        self._text_cptb = tk.Label(self._cadre_accueil, text="LE COMPTE EST BON", font=("Courrier", 40), bg = la_couleur_du_fond, fg="white").pack()
        self._text_commencer = tk.Label(self._cadre_accueil, text="~ Commencer une partie en choisissant une des options ci-dessous ~", font=("Courrier", 10), bg = la_couleur_du_fond, fg="white").pack()
        
        #Ajouter du buton
        self._buton_entrainement =  tk.Button(self._cadre_accueil, text="Entrainement", font=("Courrier", 20), bg = "white", fg = la_couleur_du_fond,  command = self.formulaire_creation_joueur).pack(pady=10, fill="x")
        self._buton_jeu_a_deux =  tk.Button(self._cadre_accueil, text="Jeu à deux", font=("Courrier", 20), bg = "white", fg = la_couleur_du_fond).pack(pady=10, fill="x")
        """
        
    
    def formulaire_creation_joueur(self):
        """
            Cette methode affiche le formulaire de renseignement du pseudo Gamer
        """
        #on cache le cadre d'accueil
        self._cadre_accueil.pack_forget()
        
        #creation des nouveaux cadres pour la creation d'un joueur
        self._cadre_creation_p = tk.Frame(self,  bg = la_couleur_du_fond)
        self._cadre_creation = tk.Frame(self._cadre_creation_p,  bg = la_couleur_du_fond) 
        self._cadre_creation_2 = tk.Frame(self._cadre_creation_p,  bg = la_couleur_du_fond) 
        self._cadre_creation_3 = tk.Frame(self._cadre_creation_p,  bg = la_couleur_du_fond)
        
        #Formulaire de création d'un joueur
        _label_info = tk.Label(self._cadre_creation, text="~ Veuillez renseigner votre pseudo, ce champ est obligatoir * ~", font=("Courrier", 10), bg = la_couleur_du_fond, fg="white").pack()
        _label_nom = tk.Label(self._cadre_creation, text="Pseudo :", font=("Courrier", 10), bg = la_couleur_du_fond, fg="white").pack()
        
        #Ajout de l'icone connexion
        self._t_icon = (50,50)
        self._image = tk.PhotoImage(file = le_path_img_connexion).zoom(20).subsample(18)
        
        _canvas = tk.Canvas(self._cadre_creation_2, width = self._t_icon[0], height=self._t_icon[1], bg = la_couleur_du_fond, bd=0, highlightthickness=0)
        _canvas.create_image(self._t_icon[0]/2, self._t_icon[1]/2, image = self._image)
        _canvas.grid(row=0, column=0, sticky="w")
        
        #Variable de controle pour récupérer le nom saisie
        self._var_nom = tk.StringVar()
        self._champ_nom = tk.Entry(self._cadre_creation_2, font=("Courrier", 18), textvariable=self._var_nom).grid(row=0, column = 1, sticky="w")
        
        #Le bouton d'creation
        _buton_creer =Button(self._cadre_creation_3)
        _buton_creer.fixer_label_du_button("Connexion")
        _buton_creer.fixer_une_callback(self.creer_joueur)
        _buton_creer.fixer_une_option(font=("Courrier", 10), bg = "white", fg = la_couleur_du_fond)
        _buton_creer.pack(pady=5, padx=5, fill="both")
        
        self._cadre_creation.pack(side="top")
        self._cadre_creation_2.pack( side="top")
        self._cadre_creation_3.pack( side="top")
        self._cadre_creation_p.pack( expand = "yes")
        
    def creer_joueur(self):
        """
            Fonction callback du buton connexion 
                si le champ est vide elle lance une fenetre d'info
                sinon elle enregistre le joueur (enfin créé le joueur)
        """
        if len(self._var_nom.get()) == 0 :
            self.lance_alert("Le champ ne doit pas être vide, veuillez renseigner un pseudo!")
        else:
            self._controller.enregistrer_joueur_et_lancer_entrainement(self._var_nom.get()) #recupère le pseudo saisie et on enregistre
    
           
    def interface_du_entrainement(self, tirage):
        print(tirage)
        
        #on cache l'interface d'creation
        self._cadre_creation_p.pack_forget()
        
        #la grande section où sont inclus le frame inter_tirage
        self._interface = tk.Frame(self, bg = la_couleur_du_fond, bd=2, relief="sunken")
        self._inter_solution = tk.Frame(self, bg = la_couleur_du_fond, bd=2, relief="sunken")
        self._inter_Historique = tk.Frame(self, bg = la_couleur_du_fond, bd=2, relief="sunken", padx=10, pady=10)
        
        #les sous sections
        self._inter_tirage = tk.Frame(self._interface, bg = la_couleur_du_fond)
        self._inter_effectuer_operation = tk.Frame(self._interface, bg = la_couleur_du_fond) #le bouton effectuer l'opération
        
        
        #les listes box des plaques et les opérateurs
        self._listbox_des_plaques = tk.Listbox(self._inter_tirage, exportselection=0, selectmode=EXTENDED, activestyle='none')
        self._listbox_des_operateurs = tk.Listbox(self._inter_tirage, exportselection=0, activestyle='none')
        
        self._listbox_operation = tk.Listbox(self._inter_Historique, exportselection=0, selectmode=EXTENDED, activestyle='none')
       
        #le boutton effectué l'opération
        self._buton_effectuer_operation = tk.Button(self._inter_effectuer_operation, text="Effectuer", command=lambda:self._controller.effectuer_operation(self._listbox_des_plaques.curselection(), self._listbox_des_operateurs.curselection()))
       
        
        self._le_nombre_N = tk.Label(self._inter_solution, text="154", font=("Courrier", 25), bg = "white", fg = la_couleur_du_fond)
        self._buton_solution = tk.Button(self._inter_solution, text="Solution", font=("Courrier", 15), bg = "white", fg = la_couleur_du_fond)
        
        
        self._label_historique = tk.Label(self._inter_Historique, text="HISTORIQUE")
        self._bouton_supprimer_operation = Button(self._inter_Historique)
        self._bouton_supprimer_operation.fixer_label_du_button("Suppr opération")
        self._bouton_supprimer_operation.fixer_une_callback(self._controller.supprimer_derniere_operation)
        self._bouton_supprimer_operation.fixer_une_option(font=("Courrier", 15), bg = "white", fg = la_couleur_du_fond)
        
        #les items de la listbox des plaques
        for i in range(0,6):
            self._listbox_des_plaques.insert(i, "{}".format(tirage[i]))
            
        #les items de la listbox des opérateurs
        for i in range(0,4):
            self._listbox_des_operateurs.insert(i, "{}".format(self._controller.liste_operateur()[i]))
        
        
        self._interface.grid(row=0, column=0)
        self._inter_solution.grid(row=0, column=1, sticky = "ns", padx=5, pady=5)
        self._inter_Historique.grid(row=2, column=0)
        
        self._inter_tirage.pack()
        self._listbox_des_plaques.pack(side = LEFT)
        self._listbox_des_operateurs.pack(side = LEFT)
        self._inter_effectuer_operation.pack()
        
        
        self._buton_effectuer_operation .pack()
        self._le_nombre_N.pack(padx=10, pady=5, fill= "both")
        self._buton_solution.pack()
        self._label_historique.pack()
        self._listbox_operation.pack()
        self._bouton_supprimer_operation.pack()
    
    
    def lance_alert(self, msg):
        #Lance une boites de dialogue info
        messagebox.showinfo("Information", msg)
        
    def ajouter_listbox_plaque(self,element):
        """
            Cette methode ajoute un élément de la listebox des plaques (à la fin)
        """
        self._listbox_des_plaques.insert('end', element)
    
    def ajouter_listbox_operation(self, element):
        """
            Cette methode ajoute un élément de la listebox operation (à la fin)
        """
        self._listbox_operation.insert('end', element)
        
    def supprimer_item_listbox_plaque(self, index):
        """
            Supprime un élément de la listbox des plaques à la position (index) donné en paramètre
        """
        self._listbox_des_plaques.delete(index)
        
    def supprimer_dernier_listbox_operation(self):
        """
            Supprime la dernière line de la listebox opération
        """
        self._listbox_operation.delete('end')
    def supprimer_une_plaque(self, element):
        """
            cette methode supprime la plaque (element) de la listbox des plaque
        """
        les_element = self._listbox_des_plaques.get(0, 'end')
        for i in range(0, len(les_element)):
            if int(les_element[i]) == element:
                self._listbox_des_plaques.delete(i)