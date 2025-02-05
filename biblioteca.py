import customtkinter as ctk
from tkinter import messagebox

class Livro:
    livros = [] # Array

    def __init__(self, titulo, autor, editora, ano, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.genero = genero
        self.paginas = paginas

    @classmethod
    def cadastrar(cls, parent_frame, main_frame): # Cadastrar livro
        '''Função para cadastrar um novo livro.'''
        def submit():
            '''Função para submeter o cadastro do livro.'''
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            editora = entry_editora.get()
            ano = entry_ano.get()
            genero = entry_genero.get()
            paginas = entry_paginas.get()
            
            novo_livro = Livro(titulo, autor, editora, ano, genero, paginas)
            cls.livros.append(novo_livro)
            messagebox.showinfo("Cadastro de Livro", f"O livro '{titulo}' foi cadastrado com sucesso!")
            cadastro_frame.pack_forget()
            main_frame.pack(fill="both", expand=True)

        parent_frame.pack_forget()
        cadastro_frame = ctk.CTkFrame(parent_frame.master)
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

    @classmethod
    def listar_livros(cls): # Listar livros
        '''Função para listar os livros cadastrados.'''
        if not cls.livros:
            cls.show_message("Listar Livros", "Nenhum livro cadastrado.")
        else:
            livros_str = "\n".join([f"{livro.titulo} por {livro.autor}" for livro in cls.livros])
            cls.show_message("Listar Livros", livros_str)

    @classmethod
    def pesquisar_livro(cls): # Pesquisar livro
        '''Função para pesquisar um livro pelo título.'''
        titulo = ctk.CTkInputDialog(text="Digite o título do livro que deseja pesquisar:", title="Pesquisar Livro").get_input()
        for livro in cls.livros:
            if livro.titulo == titulo:
                cls.show_message("Pesquisar Livro", f"O livro '{titulo}' com o autor '{livro.autor}' foi encontrado.")
                return
        cls.show_message("Pesquisar Livro", f"O livro '{titulo}' não foi encontrado.")
    
    @classmethod
    def deletar_livro(cls): # Deletar livro
        '''Função para deletar um livro pelo título.'''
        titulo = ctk.CTkInputDialog(text="Digite o título do livro que deseja deletar:", title="Deletar Livro").get_input()
        for livro in cls.livros:
            if livro.titulo == titulo:
                cls.livros.remove(livro)
                cls.show_message("Deletar Livro", f"O livro '{titulo}' foi deletado com sucesso.")
                return
        cls.show_message("Deletar Livro", f"O livro '{titulo}' não foi encontrado.")

    @staticmethod
    def show_message(title, message):
        window = ctk.CTkToplevel()
        window.title(title)
        window.geometry("400x300")
        textbox = ctk.CTkTextbox(window, width=380, height=260)
        textbox.pack(pady=20)
        textbox.insert("0.0", message)
        textbox.configure(state="disabled")

# Livro para cadastro inicial
Livro.livros.append(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "HarperCollins", 1954, "Fantasia", 1216))