#coding:utf-8
'''
Created on 26 mars 2020

@author: X
'''
from Constants import la_couleur_du_fond
from Button import Button
"""
    Ce module defini deux m�thodes qui assure la vue d'accueil de l'application
"""

def les_labels_accueil(le_frame_parent, tk):
    tk.Label(le_frame_parent, text="Bienvenue sur le jeu de Maths", font=("Courrier", 25), bg = la_couleur_du_fond, fg="white").pack()
    tk.Label(le_frame_parent, text="LE COMPTE EST BON", font=("Courrier", 40), bg = la_couleur_du_fond, fg="white").pack()
    tk.Label(le_frame_parent, text="~ Commencer une partie en choisissant une des options ci-dessous ~", font=("Courrier", 10), bg = la_couleur_du_fond, fg="white").pack()

def les_button_accueil(le_frame_parent, *f_callback):
    
    bouton_entrainement = Button(le_frame_parent)
    bouton_entrainement.fixer_label_du_button("Entrainement")
    bouton_entrainement.fixer_une_callback(f_callback[0])
    bouton_entrainement.fixer_une_option(font=("Courrier", 20), bg = "white", fg = la_couleur_du_fond)
    
    bouton_entrainement.pack(pady=10, fill="x")
    
    bouton_jeu_a_deux = Button(le_frame_parent)
    bouton_jeu_a_deux.fixer_label_du_button("Jeu à deux")
    bouton_jeu_a_deux.fixer_une_callback(f_callback[0])
    bouton_jeu_a_deux.fixer_une_option(font=("Courrier", 20), bg = "white", fg = la_couleur_du_fond)
    
    bouton_jeu_a_deux.pack(pady=10, fill="x")