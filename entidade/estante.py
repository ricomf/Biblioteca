# import customtkinter as ctk
# from tkinter import messagebox
# import unicodedata
# from entidade.livro import Livro

# class Estante:
#     estantes = []

#     def __init__(self, nome):
#         self.nome = nome
#         self.livros = []

#     def adicionar_livro(self, livro):
#         self.livros.append(livro)

#     def listar_livros(self):
#         if not self.livros:
#             Estante.show_message("Listar Livros", "Nenhum livro cadastrado.")
#         else:
#             livros_str = "\n".join([f"{livro.titulo} por {livro.autor}" for livro in self.livros])
#             Estante.show_message("Listar Livros", livros_str)

#     # @classmethod
#     # def criar_estante(cls, nome):
#     #     nova_estante = Estante(nome)
#     #     cls.estantes.append(nova_estante)
#     #     messagebox.showinfo("Criar Estante", f"A estante '{nome}' foi criada com sucesso!")

#     # @classmethod
#     # def listar_estantes(cls):
#     #     if not cls.estantes:
#     #         cls.show_message("Listar Estantes", "Nenhuma estante criada.")
#     #     else:
#     #         estantes_str = "\n".join([estante.nome for estante in cls.estantes])
#     #         cls.show_message("Listar Estantes", estantes_str)

#     # @staticmethod
#     # def remover_acentos(texto):
#     #     return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

#     # @staticmethod
#     # def show_message(title, message):
#     #     window = ctk.CTkToplevel()
#     #     window.title(title)
#     #     window.geometry("400x300")
#     #     textbox = ctk.CTkTextbox(window, width=380, height=260)
#     #     textbox.pack(pady=20)
#     #     textbox.insert("0.0", message)
#     #     textbox.configure(state="disabled")
    
