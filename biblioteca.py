import customtkinter as ctk

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
        titulo = ctk.CTkInputDialog(text="Digite o título do livro:", title="Cadastro de Livro").get_input()
        autor = ctk.CTkInputDialog(text="Digite o autor do livro:", title="Cadastro de Livro").get_input()
        editora = ctk.CTkInputDialog(text="Digite a editora do livro:", title="Cadastro de Livro").get_input()
        ano = ctk.CTkInputDialog(text="Digite o ano de publicação do livro:", title="Cadastro de Livro").get_input()
        genero = ctk.CTkInputDialog(text="Digite o gênero do livro:", title="Cadastro de Livro").get_input()
        paginas = ctk.CTkInputDialog(text="Digite o número de páginas do livro:", title="Cadastro de Livro").get_input()
        
        novo_livro = Livro(titulo, autor, editora, ano, genero, paginas)
        cls.livros.append(novo_livro)
        cls.show_message("Cadastro de Livro", f"O livro '{titulo}' foi cadastrado com sucesso!")

    @classmethod
    def listar_livros(cls):
        if not cls.livros:
            cls.show_message("Listar Livros", "Nenhum livro cadastrado.")
        else:
            livros_str = "\n".join([f"{livro.titulo} por {livro.autor}" for livro in cls.livros])
            cls.show_message("Listar Livros", livros_str)

    @classmethod
    def pesquisar_livro(cls):
        titulo = ctk.CTkInputDialog(text="Digite o título do livro que deseja pesquisar:", title="Pesquisar Livro").get_input()
        for livro in cls.livros:
            if livro.titulo == titulo:
                cls.show_message("Pesquisar Livro", f"O livro '{titulo}' com o autor '{livro.autor}' foi encontrado.")
                return
        cls.show_message("Pesquisar Livro", f"O livro '{titulo}' não foi encontrado.")
    
    @classmethod
    def deletar_livro(cls):
        titulo = ctk.CTkInputDialog(text="Digite o título do livro que deseja deletar:", title="Deletar Livro").get_input()
        for livro in cls.livros:
            if livro.titulo == titulo.title():
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