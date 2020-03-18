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

class Vue(tk.Tk):
    '''
        
    '''

    color_fond = "#212F3C"
    taille_fenetre = (720,480)
    tple_operateur = ("+","-","*","/")
    
    def __init__(self, controller):
        '''
        Constructor
        '''
        tk.Tk.__init__(self)
        
        #Définition du titre, fond, logo de la fenetre principale
        self.title("LE COMPTE EST BON")
        self.iconbitmap("img/logo.ico")
        self.config(bg = Vue.color_fond)
        
        self._controller = controller #instance du controller
        
        #appel de quelques methodes qui definissent les propriétés de la fenetre principale
        self.taille_de_la_fenetre()     #On fixe la taille
        self.accueil()                  #Le text d'accueil et le bouton lancé une partie
    
    def taille_de_la_fenetre(self):
        self.geometry(f"{Vue.taille_fenetre[0]}x{Vue.taille_fenetre[1]}")
        self.resizable(width = False, height = False)
        
    def accueil(self):
        self._cadre_accueil = tk.Frame(self, bg = Vue.color_fond)
        
        #Ajouter du text d'accueil
        self._text_accueil = tk.Label(self._cadre_accueil, text="Bienvenue sur le jeu de Maths", font=("Courrier", 25), bg = Vue.color_fond, fg="white").pack()
        self._text_cptb = tk.Label(self._cadre_accueil, text="LE COMPTE EST BON", font=("Courrier", 40), bg = Vue.color_fond, fg="white").pack()
        self._text_commencer = tk.Label(self._cadre_accueil, text="~ Commencer une partie en choisissant une des options ci-dessous ~", font=("Courrier", 10), bg = Vue.color_fond, fg="white").pack()
        
        #Ajouter du buton
        self._buton_entrainement =  tk.Button(self._cadre_accueil, text="Entrainement", font=("Courrier", 20), bg = "white", fg = Vue.color_fond,  command = self.formulaire_creation_joueur).pack(pady=10, fill="x")
        self._buton_jeu_a_deux =  tk.Button(self._cadre_accueil, text="Jeu à deux", font=("Courrier", 20), bg = "white", fg = Vue.color_fond).pack(pady=10, fill="x")
        
        self._cadre_accueil.pack(expand="yes")
    
    def formulaire_creation_joueur(self):
        #on cache le cadre d'accueil
        self._cadre_accueil.pack_forget()
        
        #creation des nouveaux cadres pour l'enregistrement
        self._cadre_enregistrement_p = tk.Frame(self,  bg = Vue.color_fond)
        self._cadre_enregistrement = tk.Frame(self._cadre_enregistrement_p,  bg = Vue.color_fond) 
        self._cadre_enregistrement_2 = tk.Frame(self._cadre_enregistrement_p,  bg = Vue.color_fond) 
        self._cadre_enregistrement_3 = tk.Frame(self._cadre_enregistrement_p,  bg = Vue.color_fond)
        
        #Formulaire d'enregistrement
        self._label_info = tk.Label(self._cadre_enregistrement, text="~ Veuillez renseigner votre pseudo, ce champ est obligatoir * ~", font=("Courrier", 10), bg = Vue.color_fond, fg="white").pack()
        self._label_nom = tk.Label(self._cadre_enregistrement, text="Pseudo :", font=("Courrier", 10), bg = Vue.color_fond, fg="white").pack()
        
        #Ajout de l'icone connexion
        self._t_icon = (50,50)
        self._image = tk.PhotoImage(file="img/icon_connexion.png").zoom(20).subsample(18)
        
        self._canvas = tk.Canvas(self._cadre_enregistrement_2, width = self._t_icon[0], height=self._t_icon[1], bg = Vue.color_fond, bd=0, highlightthickness=0)
        self._canvas.create_image(self._t_icon[0]/2, self._t_icon[1]/2, image = self._image)
        
        self._canvas.grid(row=0, column=0, sticky="w")
        #Variable de controle
        self._var_nom = tk.StringVar()
        self._champ_nom = tk.Entry(self._cadre_enregistrement_2, font=("Courrier", 18), textvariable=self._var_nom).grid(row=0, column = 1, sticky="w")
        
        self._buton_enregistrer = tk.Button(self._cadre_enregistrement_3, text="Connexion", font=("Courrier", 10), bg = "white", fg = Vue.color_fond, command=self.creer_joueur_mode_entraienement).pack(pady=5, padx=5, fill="both")
        
        self._cadre_enregistrement.pack(side="top")
        self._cadre_enregistrement_2.pack( side="top")
        self._cadre_enregistrement_3.pack( side="top")
        self._cadre_enregistrement_p.pack( expand = "yes")
        
    def creer_joueur_mode_entraienement(self):
        if len(self._var_nom.get()) == 0 :
            messagebox.showinfo("Champ vide!", "Le champ ne doit pas être vide, veuillez renseigner un pseudo!")
        else:
            self._controller.creer_joueur_mode_entrainement(self._var_nom.get()) #recupère le pseudo saisie et on enregistre
            self.interface_du_entrainement(self._controller.tirage())  #appelle interface d'entrainement
            
    def interface_du_entrainement(self, tirage):
        print(tirage)
        
        #on cache l'interface d'enregistrement
        self._cadre_enregistrement_p.pack_forget()
        
        #la grande section où sont inclus le frame inter_tirage
        self._interface = tk.Frame(self, bg = Vue.color_fond, bd=2, relief="sunken")
        self._inter_solution = tk.Frame(self, bg = Vue.color_fond, bd=2, relief="sunken")
        self._inter_Historique = tk.Frame(self, bg = Vue.color_fond, bd=2, relief="sunken", padx=10, pady=10)
        
        #les sous sections
        self._inter_tirage = tk.Frame(self._interface, bg = Vue.color_fond)
        self._inter_effectuer_operation = tk.Frame(self._interface, bg = Vue.color_fond) #le bouton effectuer l'opération
        
        
        #les listes box des plaques et les opérateurs
        self._listbox_des_plaques = tk.Listbox(self._inter_tirage, exportselection=0, selectmode=EXTENDED, activestyle='none')
        self._listbox_des_operateurs = tk.Listbox(self._inter_tirage, exportselection=0, activestyle='none')
        
        #le boutton effectué l'opération
        self._buton_effectuer_operation = tk.Button(self._inter_effectuer_operation, text="Effectuer", command=self.get_index)
        self._le_nombre_N = tk.Label(self._inter_solution, text="154", font=("Courrier", 25), bg = "white", fg = Vue.color_fond)
        self._buton_solution = tk.Button(self._inter_solution, text="Solution", font=("Courrier", 15), bg = "white", fg = Vue.color_fond)
        
        
        self._label_historique = tk.Label(self._inter_Historique, text="HISTORIQUE")
        #les items de la listbox des plaques
        for i in range(0,6):
            self._listbox_des_plaques.insert(i, "{}".format(tirage[i]))
            
        #les items de la listbox des opérateurs
        for i in range(0,4):
            self._listbox_des_operateurs.insert(i, "{}".format(Vue.tple_operateur[i]))
        
        
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
    
    def get_index(self):
        print("Vous avez selectionner la plaque numéro : {} => 1erOperande".format(int(self._listbox_des_plaques.curselection()[0]+1)))
        print("Et l'opérateur numéro : {}".format(int(self._listbox_des_operateurs.curselection()[0]+1)))
        print("Vous avez selectionner la plaque numéro : {} => 2emOperande".format(int(self._listbox_des_plaques.curselection()[1]+1)))
        