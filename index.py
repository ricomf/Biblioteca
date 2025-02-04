from biblioteca import Livro
from utils.utils import limpar_tela

print("Escolha a opção que deseja\n------------------")
while True:
    
    print("\n1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Deletar um Livro")
    print("4 - Editar um Livro")
    print("4 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        Livro.cadastrar()
        
    elif opcao == '2': 
        print("\nGostaria de pesquisar por um livro ou deseja listar todos?")
        resposta = input("Digite 'pesquisar' ou 'listar': ")
        if resposta == 'pesquisar':
            titulo = input("Digite o título do livro: ")
            for livro in Livro.livros:
                if livro.titulo == titulo.title():
                    print(f"\n(o autor {livro.autor} escreveu o livro {livro.titulo} em {livro.ano} e ele tem {livro.paginas} páginas.)")
                    break
            else:
                print(f"O livro {titulo} não foi encontrado.")
                
        elif resposta == 'listar':
            if not Livro.livros:
                print("(Nenhum livro cadastrado.)")
            else:
                Livro.listar_livros()
            
        else:
            print("Opção inválida.")
    
    elif opcao == '3':
        Livro.deletar_livro()
        
    elif opcao == '4':
        limpar_tela()
        break
    
            
        