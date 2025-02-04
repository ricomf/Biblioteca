import tkinter as tk
from tkinter import messagebox, simpledialog

class Livro:
    livros = []

    def __init__(self, titulo, autor, editora, ano, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.genero = genero
        self.paginas = paginas

    @classmethod
    def cadastrar(cls):
        titulo = simpledialog.askstring("Cadastro de Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Cadastro de Livro", "Digite o autor do livro:")
        editora = simpledialog.askstring("Cadastro de Livro", "Digite a editora do livro:")
        ano = simpledialog.askinteger("Cadastro de Livro", "Digite o ano de publicação do livro:")
        genero = simpledialog.askstring("Cadastro de Livro", "Digite o gênero do livro:")
        paginas = simpledialog.askinteger("Cadastro de Livro", "Digite o número de páginas do livro:")
        
        novo_livro = Livro(titulo, autor, editora, ano, genero, paginas)
        cls.livros.append(novo_livro)
        messagebox.showinfo("Cadastro de Livro", f"O livro '{titulo}' foi cadastrado com sucesso!")

    @classmethod
    def listar_livros(cls):
        if not cls.livros:
            messagebox.showinfo("Listar Livros", "Nenhum livro cadastrado.")
        else:
            livros_str = "\n".join([f"{livro.titulo} por {livro.autor}" for livro in cls.livros])
            messagebox.showinfo("Listar Livros", livros_str)

    @classmethod
    def pesquisar_livro(cls):
        titulo = simpledialog.askstring("Pesquisar Livro", "Digite o título do livro que deseja pesquisar:")
        for livro in cls.livros:
            print(cls.livros)
            if livro.titulo == titulo:
                messagebox.showinfo("Pesquisar Livro", f"O livro '{titulo}' com o autor '{livro.autor}' foi encontrado.")
                return
        messagebox.showinfo("Pesquisar Livro", f"O livro '{titulo}' não foi encontrado.")
    
    @classmethod
    def deletar_livro(cls):
        titulo = simpledialog.askstring("Deletar Livro", "Digite o título do livro que deseja deletar:")
        for livro in cls.livros:
            if livro.titulo == titulo.title():
                cls.livros.remove(livro)
                messagebox.showinfo("Deletar Livro", f"O livro '{titulo}' foi deletado com sucesso.")
                return
        messagebox.showinfo("Deletar Livro", f"O livro '{titulo}' não foi encontrado.")

# Livro para cadastro inicial
Livro.livros.append(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "HarperCollins", 1954, "Fantasia", 1216))