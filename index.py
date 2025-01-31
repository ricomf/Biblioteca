from biblioteca import Livro

print("Escolha a opção que deseja\n------------------")
while True:
    
    print("\n1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        Livro.cadastrar()
        
    elif opcao == '2':
        Livro.listar_livros()
        print("\nGostaria de ver quantas páginas tem algum livro?")
        resposta = input("Digite 'sim' ou 'não': ")
        if resposta == 'sim':
            titulo = input("Digite o título do livro: ")
            for livro in Livro.livros:
                if livro.titulo == titulo.title():
                    print(f"\n(O livro {livro.titulo} tem {livro.paginas} páginas.)")
                    break
            else:
                print(f"O livro {titulo} não foi encontrado.")
        elif resposta == 'não':
            pass
        else:
            print("Opção inválida.")
    
    elif opcao == '3':
        break
    
            
        