from tkinter import messagebox
from entidade.livro import Livro

class Listar:
    def __init__(self):
        pass
    
    def listar_livros():
        if not Livro.lista_livros:
            messagebox.showinfo("Listar Livros", "Nenhum livro cadastrado.")
        else:
            livros_str = "\n".join([f"{livro.titulo} ({livro.ano}) - {livro.autor}" for livro in Livro.lista_livros])
            messagebox.showinfo("Listar Livros", livros_str)