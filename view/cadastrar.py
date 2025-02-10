from entidade.livro import Livro
import customtkinter as ctk
from tkinter import messagebox

class Cadastro:
    def __init__(self, parent_frame, main_frame):
        self.parent_frame = parent_frame
        self.main_frame = main_frame

    def cadastrar(self):
        def submit():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            editora = entry_editora.get()
            ano = entry_ano.get()
            genero = entry_genero.get()
            paginas = entry_paginas.get()
            
            novo_livro = Livro(titulo, autor, editora, ano, genero, paginas)
            Livro.adicionar_livro(novo_livro)
            messagebox.showinfo("Cadastro de Livro", f"O livro '{titulo}' foi cadastrado com sucesso!")
            cadastro_frame.pack_forget()
            self.main_frame.pack(fill="both", expand=True)

        self.parent_frame.pack_forget()
        cadastro_frame = ctk.CTkFrame(self.parent_frame.master)
        cadastro_frame.pack(fill="both", expand=True)

        label_titulo = ctk.CTkLabel(cadastro_frame, text="Título:")
        label_titulo.pack(pady=5)
        entry_titulo = ctk.CTkEntry(cadastro_frame)
        entry_titulo.pack(pady=5)

        label_autor = ctk.CTkLabel(cadastro_frame, text="Autor:")
        label_autor.pack(pady=5)
        entry_autor = ctk.CTkEntry(cadastro_frame)
        entry_autor.pack(pady=5)

        label_editora = ctk.CTkLabel(cadastro_frame, text="Editora:")
        label_editora.pack(pady=5)
        entry_editora = ctk.CTkEntry(cadastro_frame)
        entry_editora.pack(pady=5)

        label_ano = ctk.CTkLabel(cadastro_frame, text="Ano:")
        label_ano.pack(pady=5)
        entry_ano = ctk.CTkEntry(cadastro_frame)
        entry_ano.pack(pady=5)

        label_genero = ctk.CTkLabel(cadastro_frame, text="Gênero:")
        label_genero.pack(pady=5)
        entry_genero = ctk.CTkEntry(cadastro_frame)
        entry_genero.pack(pady=5)

        label_paginas = ctk.CTkLabel(cadastro_frame, text="Páginas:")
        label_paginas.pack(pady=5)
        entry_paginas = ctk.CTkEntry(cadastro_frame)
        entry_paginas.pack(pady=5)

        btn_submit = ctk.CTkButton(cadastro_frame, text="Cadastrar", command=submit)
        btn_submit.pack(pady=20)