from entidade.livro import Livro
import customtkinter as ctk
from tkinter import messagebox


class Cadastro:
    def __init__(self, parent_frame, main_frame):
        self.parent_frame = parent_frame
        self.main_frame = main_frame
    
    def submit(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        editora = self.entry_editora.get()
        ano = self.entry_ano.get()
        genero = self.entry_genero.get()
        paginas = self.entry_paginas.get()
        
        novo_livro = Livro(titulo, autor, editora, ano, genero, paginas)
        Livro.livros.append(novo_livro)
        messagebox.showinfo("Cadastro de Livro", f"O livro '{titulo}' foi cadastrado com sucesso!")
        self.cadastro_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)
    
    def cadastrar(self):
        self.parent_frame.pack_forget()
        self.cadastro_frame = ctk.CTkFrame(self.parent_frame.master)
        self.cadastro_frame.pack(fill="both", expand=True)
        
        self.label_titulo = ctk.CTkLabel(self.cadastro_frame, text="Título:")
        self.label_titulo.pack(pady=5)
        self.entry_titulo = ctk.CTkEntry(self.cadastro_frame)
        self.entry_titulo.pack(pady=5)
        
        self.label_autor = ctk.CTkLabel(self.cadastro_frame, text="Autor:")
        self.label_autor.pack(pady=5)
        self.entry_autor = ctk.CTkEntry(self.cadastro_frame)
        self.entry_autor.pack(pady=5)
        
        self.label_editora = ctk.CTkLabel(self.cadastro_frame, text="Editora:")
        self.label_editora.pack(pady=5)
        self.entry_editora = ctk.CTkEntry(self.cadastro_frame)
        self.entry_editora.pack(pady=5)
        
        self.label_ano = ctk.CTkLabel(self.cadastro_frame, text="Ano:")
        self.label_ano.pack(pady=5)
        self.entry_ano = ctk.CTkEntry(self.cadastro_frame)
        self.entry_ano.pack(pady=5)
        
        self.label_genero = ctk.CTkLabel(self.cadastro_frame, text="Gênero:")
        self.label_genero.pack(pady=5)
        self.entry_genero = ctk.CTkEntry(self.cadastro_frame)
        self.entry_genero.pack(pady=5)
        
        self.label_paginas = ctk.CTkLabel(self.cadastro_frame, text="Páginas:")
        self.label_paginas.pack(pady=5)
        self.entry_paginas = ctk.CTkEntry(self.cadastro_frame)
        self.entry_paginas.pack(pady=5)
        
        btn_submit = ctk.CTkButton(self.cadastro_frame, text="Cadastrar",
                                   command=self.submit, fg_color="gray20",
                                   hover_color="gray30", border_color="gray20",
                                   border_width=0)
        btn_submit.pack(pady=20)