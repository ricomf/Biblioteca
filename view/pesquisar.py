from entidade.livro import Livro
import customtkinter as ctk
from tkinter import messagebox
import unicodedata

class Pesquisar:
    def __init__(self):
        pass

    @staticmethod
    def remover_acentos(texto):
        return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

    @staticmethod
    def pesquisar_livro():
        titulo = ctk.CTkInputDialog(text="Digite o título do livro:", title="Pesquisar Livro").get_input()
        
        if not titulo:
            messagebox.showinfo("Pesquisar Livro", "Nenhum título foi inserido.")
            return
        
        titulo = Pesquisar.remover_acentos(titulo.strip().lower())
        resultados = [livro for livro in Livro.lista_livros if titulo in Pesquisar.remover_acentos(livro.titulo.strip().lower())]
        
        if resultados:
            livros_str = "\n".join([f"{livro.titulo} ({livro.ano}) - {livro.autor}" for livro in resultados])
            messagebox.showinfo("Pesquisar Livro", livros_str)
        else:
            messagebox.showinfo("Pesquisar Livro", f"Nenhum livro encontrado com '{titulo}'.")

