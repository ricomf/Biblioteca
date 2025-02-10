import sqlite3

class Livro:
    def __init__(self, titulo, autor, editora, ano, genero, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.genero = genero
        self.paginas = paginas

    @staticmethod
    def criar_tabela():
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                editora TEXT NOT NULL,
                ano INTEGER NOT NULL,
                genero TEXT NOT NULL,
                paginas INTEGER NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def adicionar_livro(livro):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO livros (titulo, autor, editora, ano, genero, paginas)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (livro.titulo, livro.autor, livro.editora, livro.ano, livro.genero, livro.paginas))
        conn.commit()
        conn.close()

    @staticmethod
    def listar_livros():
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros')
        livros = cursor.fetchall()
        conn.close()
        return livros

    @staticmethod
    def pesquisar_livro(titulo):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM livros WHERE titulo LIKE ?', ('%' + titulo + '%',))
        livros = cursor.fetchall()
        conn.close()
        return livros

    @staticmethod
    def deletar_livro(titulo):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM livros WHERE titulo LIKE ?', ('%' + titulo + '%',))
        conn.commit()
        conn.close()