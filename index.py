import tkinter as tk
from biblioteca import Livro

def main():
    root = tk.Tk()
    root.title("Sistema de Biblioteca")
    root.geometry("600x400")

    btn_cadastrar = tk.Button(root, text="Cadastrar Livro", command=Livro.cadastrar)
    btn_cadastrar.pack(pady=20)

    btn_listar = tk.Button(root, text="Listar Livros", command=Livro.listar_livros)
    btn_listar.pack(pady=20)
    
    btn_listar = tk.Button(root, text="Pesquisar Livros", command=Livro.pesquisar_livro)
    btn_listar.pack(pady=20)

    btn_deletar = tk.Button(root, text="Deletar Livro", command=Livro.deletar_livro)
    btn_deletar.pack(pady=20)

    btn_sair = tk.Button(root, text="Sair", command=root.quit)
    btn_sair.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()