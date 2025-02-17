import customtkinter as ctk
from entidade.livro import Livro
from utils.limpa_tela import Tela_Limpa
from view.cadastrar import Cadastro
from view.listar import Listar
from view.pesquisar import Pesquisar
from view.deletar import Deletar



def main():
    '''Aparencia da janela'''
    ctk.set_default_color_theme("dark-blue")  # Usa um tema escuro predefinido
    ctk.set_appearance_mode("dark")
    
    

    '''Janela'''
    janela = ctk.CTk() 
    janela.title("Sistema de Biblioteca")
    janela.geometry("600x700")

    
    
    
    '''Frame principal'''
    main_frame = ctk.CTkFrame(janela)
    main_frame.pack(fill="both", expand=True)


    '''Botões'''
    btn_cadastrar = ctk.CTkButton(main_frame, text="Cadastrar Livro",
                                  compound="left", command=lambda: Cadastro(main_frame, main_frame).cadastrar(),
                                  fg_color="gray20", hover_color="gray30",
                                  border_color="gray20", border_width=0)
    btn_cadastrar.pack(pady=20)

    btn_listar = ctk.CTkButton(main_frame, text="Listar Livros",
                               command=Listar.listar_livros, fg_color="gray20",
                               hover_color="gray30", border_color="gray20",
                               border_width=0)
    btn_listar.pack(pady=20)
    
    btn_pesquisar = ctk.CTkButton(main_frame, text="Pesquisar Livro",
                                  command=Pesquisar.pesquisar_livro, fg_color="gray20",
                                  hover_color="gray30", border_color="gray20",
                                  border_width=0)
    btn_pesquisar.pack(pady=20)

    btn_deletar = ctk.CTkButton(main_frame, text="Deletar Livro",
                                command=Deletar.deletar_livro, fg_color="gray20",
                                hover_color="gray30", border_color="gray20",
                                border_width=0)
    btn_deletar.pack(pady=20)

    btn_sair = ctk.CTkButton(main_frame, text="Sair",
                             command=janela.quit,
                             fg_color="gray20",
                             hover_color="gray30")
    btn_sair.pack(pady=30)

    janela.mainloop()
    
if __name__ == "__main__":
    livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien", "WMF Martins Fontes", 1954, "Fantasia", 576)
    livro2 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", "Rocco", 1997, "Fantasia", 309)
    livro3 = Livro("Dom Quixote", "Miguel de Cervantes", "Nova Aguilar", 1605, "Romance", 1048)
    Livro.lista_livros.extend([livro1, livro2, livro3])
    main()
    Tela_Limpa.limpar_tela()