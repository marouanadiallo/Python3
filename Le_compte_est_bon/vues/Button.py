#coding:utf-8
'''
Created on 26 mars 2020

@author: DIALLO Alpha marouana
'''
import tkinter as tk

class Button(tk.Button):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        tk.Button.__init__(self, master=master)
    
    def fixer_une_option(self, **options):
        """
            Fixe une option parmi les options qui existe pour un bouton tkinter
        """
        self.config(**options)
        
    def fixer_label_du_button(self, label):
        """
            Fixe le label du bouton 
        """
        self.fixer_une_option(text=label)
    
    def fixer_une_callback(self, fonction):
        """
            Fixe une fonction callback pour le bouton
        """
        self.fixer_une_option(command=fonction)