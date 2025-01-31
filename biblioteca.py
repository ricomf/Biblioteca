class Livro:
    livros = []
    

    
    def __init__(self, titulo, autor, editora, ano, genero, paginas):
        '''Método construtor da classe Livro.'''
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.editora = editora.title()
        self.ano = ano
        self.genero = genero.title()
        self.paginas = paginas

    @property
    def titulo_autor(self):
        '''Método para retornar o título e o autor do livro.'''
        return f"{self.titlo} - {self.autor}"

    def aumentar_paginas(self, paginas):
        '''Método para aumentar o número de páginas do livro.'''
        self.paginas += paginas
        print(f"\nO livro {self.titulo} agora tem {self.paginas} páginas.")
        
    def diminuir_paginas(self, paginas):
        '''Método para diminuir o número de páginas do livro.'''
        if self.paginas - paginas < 0:
            self.paginas = 0
            print(f"\nO livro {self.titulo} não pode ter páginas negativas.")
        else:
            self.paginas -= paginas
            print(f"\nO livro {self.titulo} agora tem {self.paginas} páginas.")
            
    @classmethod
    def cadastrar(cls):
        '''Método para cadastrar um livro.'''
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        editora = input("Digite a editora do livro: ")
        ano = input("Digite o ano de publicação do livro: ")
        genero = input("Digite o gênero do livro: ")
        paginas = int(input("Digite o número de páginas do livro: "))
        livro = cls(titulo, autor, editora, ano, genero, paginas)
        cls.livros.append(livro)
        print(f"\nO livro {titulo} foi cadastrado com sucesso!")
    
    @classmethod
    def listar_livros(cls):
        '''Método para listar os livros cadastrados.'''
        for livro in cls.livros:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}')
    
# Livro para cadastro inicial
Livro.livros.append(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "HarperCollins", 1954, "Fantasia", 1216))