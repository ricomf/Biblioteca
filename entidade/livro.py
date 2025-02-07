class Livro:
    livros = []
    
    def __init__(self, titulo, autor, editora, ano, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.genero = genero
        self.paginas = paginas
        
    def __str__(self):
        return f"{self.titulo} | ({self.ano}) | {self.autor}"
    
   