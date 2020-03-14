#coding:utf-8

'''
Created on 29 f�vr. 2020

@author: Alpha marouana DIALLO
'''
import tkinter as tk
from tkinter import messagebox
from cgitb import text
from idlelib.configdialog import font_sample_text

class Vue(tk.Tk):
    '''
        
    '''

    color_fond = "#212F3C"
    taille_fenetre = (720,480)
    
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
        self._cadre_enregistrement_p.pack_forget()
        
        self._interface = tk.Frame(self, bg = Vue.color_fond)
        
        #les sections
        self._inter_tirage = tk.Frame(self._interface, bg = Vue.color_fond)
        self._inter_N = tk.Frame(self._interface, bg = Vue.color_fond)
        
        self._inter_operateurs= tk.Frame(self._interface, bg = Vue.color_fond)
        self._inter_solution = tk.Frame(self._interface, bg = Vue.color_fond)
        
        self._inter_Historique= tk.Frame(self._interface, bg = Vue.color_fond)
        
        self._val_tirage = list()
        
        #les boutons du tirage
        for i in range(0,6):
            _tmp = tk.Button(self._inter_tirage, text=tirage[i], font=("Arial", 15))
            #_tmp.config(command = lambda:self.get_index(i))
            _tmp.grid(row = 0, column = i)
            self._val_tirage.append(_tmp)
            
        
        self._val_tirage[1].config(command = lambda:self.get_index(1))
        
        self._inter_tirage.pack()
        self._interface.pack(expand = "yes")
    
    def get_index(self, arg):
        print(arg)