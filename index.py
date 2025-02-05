import customtkinter as ctk
from biblioteca import Livro

def main():
    '''Aparencia da janela'''
    ctk.set_default_color_theme("dark-blue")  # Usa um tema escuro predefinido
    ctk.set_appearance_mode("dark")

    janela = ctk.CTk() 
    janela.title("Sistema de Biblioteca")
    janela.geometry("600x400")


    '''Botões'''
    btn_cadastrar = ctk.CTkButton(janela, text="Cadastrar Livro", command=Livro.cadastrar, fg_color="gray20", hover_color="gray30", border_color="gray20", border_width=0)
    btn_cadastrar.pack(pady=20)

    btn_listar = ctk.CTkButton(janela, text="Listar Livros", command=Livro.listar_livros, fg_color="gray20", hover_color="gray30", border_color="gray20", border_width=0)
    btn_listar.pack(pady=20)
    
    btn_pesquisar = ctk.CTkButton(janela, text="Pesquisar Livros", command=Livro.pesquisar_livro, fg_color="gray20", hover_color="gray30", border_color="gray20", border_width=0)
    btn_pesquisar.pack(pady=20)

    btn_deletar = ctk.CTkButton(janela, text="Deletar Livro", command=Livro.deletar_livro, fg_color="gray20", hover_color="gray30", border_color="gray20", border_width=0)
    btn_deletar.pack(pady=20)

    btn_sair = ctk.CTkButton(janela, text="Sair", command=janela.quit, fg_color="gray20", hover_color="gray30")
    btn_sair.pack(pady=30)

    janela.mainloop()

if __name__ == "__main__":
    main()