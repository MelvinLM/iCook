
import tkinter as tk
from tkinter import ttk


from . import Frame, RecipeFrame, SearchFrame, UpdateDBFrame, CreateRecipeFrame
from .. import Recipe


class MainFrame(ttk.Frame):

    def __init__(self):
        tk.Frame.__init__(self,None)


        self.pack(fill=tk.BOTH, expand=1)
        self.master.title("iCook, do you?")

        self.noteBook = ttk.Notebook(self)
        self.noteBook.pack(fill=tk.BOTH, expand=1)

        self.searchFrame=SearchFrame.SearchFrame(parent=self.noteBook,mainFrame=self)
        self.searchFrameID = self.noteBook.add(self.searchFrame,text="Chercher recette")

        self.recipeFrame=RecipeFrame.RecipeFrame(parent=self.noteBook,mainFrame=self)
        self.noteBook.add(self.recipeFrame,text="Recette")

        self.createRecipeFrame=CreateRecipeFrame.CreateRecipeFrame(parent=self.noteBook,mainFrame=self)
        self.noteBook.add(self.createRecipeFrame,text="Ajouter recette")

        self.updateDBFrame=UpdateDBFrame.UpdateDBFrame(parent=self.noteBook,mainFrame=self) 
        self.noteBook.add(self.updateDBFrame,text="Màj BDD")

        self.tabs = {"searchFrame":0,
                    "recipeFrame":1,
                    # "favoritesFrame":2,
                    "createRecipeFrame":2,
                    "updateDBFrame":3}

        self.getToSearchFrame()
        self.noteBook.hide(self.tabs["recipeFrame"]) 

    def getToSearchFrame(self):
        self.noteBook.select(self.tabs["searchFrame"])

    def getToSyncFrame(self):
        self.noteBook.select(self.tabs["updateDBFrame"])

    def getToRecipeFrame(self,recipe):
        assert type(recipe) is Recipe.Recipe

        self.recipeFrame.loadRecipe(recipe)
        self.noteBook.select(self.tabs["recipeFrame"])

    def getToAddRecipeFrame(self):
        self.noteBook.select(self.tabs["createRecipeFrame"])








