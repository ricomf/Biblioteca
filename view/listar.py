from entidade.livro import Livro
import customtkinter as ctk
from tkinter import messagebox

class Listar:
    def __init__(self):
        pass
    
    @staticmethod
    def listar_livros():
        livros = Livro.listar_livros()
        if not livros:
            messagebox.showinfo("Listar Livros", "Nenhum livro cadastrado.")
        else:
            livros_str = "\n".join([f"{livro[1]} ({livro[4]}) - {livro[2]}" for livro in livros])
            messagebox.showinfo("Listar Livros", livros_str)