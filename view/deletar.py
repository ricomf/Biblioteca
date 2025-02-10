from entidade.livro import Livro
import customtkinter as ctk
from tkinter import messagebox
import unicodedata

class Deletar:
    def __init__(self):
        pass
    
    @staticmethod
    def remover_acentos(texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    @staticmethod
    def deletar_livro():
        titulo = ctk.CTkInputDialog(text="Digite o título do livro que deseja deletar:", title="Deletar Livro").get_input()

        if not titulo:
            messagebox.showinfo("Deletar Livro", "Nenhum título foi inserido.")
            return

        titulo = Deletar.remover_acentos(titulo.strip().lower())
        Livro.deletar_livro(titulo)
        messagebox.showinfo("Deletar Livro", "Livro deletado com sucesso.")