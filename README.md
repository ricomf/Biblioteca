# Resumo do Projeto Biblioteca

## Descrição
Este projeto consiste em um sistema simples de gerenciamento de livros, onde o usuário pode cadastrar novos livros, listar os livros cadastrados e verificar o número de páginas de um livro específico. O projeto é composto por dois arquivos principais: `biblioteca.py` e `index.py`.

## Arquivo: biblioteca.py
O arquivo `biblioteca.py` contém a definição da classe `Livro`, que representa um livro com atributos como título, autor, editora, ano de publicação, gênero e número de páginas. A classe também contém métodos para manipular esses atributos e para cadastrar e listar livros.

### Classe Livro
#### Atributos:
- `livros`: Lista de classe que armazena todos os livros cadastrados.
- `titulo`: Título do livro.
- `autor`: Autor do livro.
- `editora`: Editora do livro.
- `ano`: Ano de publicação do livro.
- `genero`: Gênero do livro.
- `paginas`: Número de páginas do livro.

#### Métodos:
- `__init__(self, titulo, autor, editora, ano, genero, paginas)`: Método construtor que inicializa os atributos do livro.
- `titulo_autor(self)`: Propriedade que retorna uma string com o título e o autor do livro.
- `aumentar_paginas(self, paginas)`: Método para aumentar o número de páginas do livro.
- `diminuir_paginas(self, paginas)`: Método para diminuir o número de páginas do livro.
- `cadastrar(cls)`: Método de classe que solicita ao usuário os detalhes do livro e o cadastra na lista de livros.
- `listar_livros(cls)`: Método de classe que lista todos os livros cadastrados.

## Arquivo: index.py
O arquivo `index.py` contém a lógica principal do programa, permitindo ao usuário interagir com o sistema de gerenciamento de livros.

### Função principal
1. Exibe um menu com opções para cadastrar livro, listar livros e sair.
2. Solicita ao usuário que escolha uma opção.
3. Executa a ação correspondente à opção escolhida:
   - `1`: Chama o método `cadastrar` da classe `Livro` para cadastrar um novo livro.
   - `2`: Chama o método `listar_livros` da classe `Livro` para listar todos os livros cadastrados e permite ao usuário verificar o número de páginas de um livro específico.
   - `3`: Encerra o programa.

### Exemplo de uso:
```python
from biblioteca import Livro

print("Escolha a opção que deseja\n------------------")
while True:
    print("1 - Cadastrar Livro")
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
                    print(f"\nO livro {livro.titulo} tem {livro.paginas} páginas.")
                    break
            else:
                print(f"O livro {titulo} não foi encontrado.")
        elif resposta == 'não':
            pass
        else:
            print("Opção inválida.")
    
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")
```
### Palavras reservadas utilizadas:
- `class`: Define uma nova classe.
- `def`: Define uma nova função ou método.
- `self`: Referência à instância atual da classe.
- `cls`: Referência à classe atual.
- `if, elif, else`: Estruturas condicionais.
- `for, in`: Estruturas de loop.
- `break`: Interrompe o loop atual.
- `continue`: Passa para a próxima iteração do loop.
- `input()`: Função que solicita entrada do usuário.
- `print()`: Função que exibe uma mensagem na tela.
- `title()`: Método de string que converte a primeira letra de cada palavra para maiúscula.
- `from`: Importa módulos ou funções específicas de um módulo.
- `import`: Importa um módulo.
- `while`: Inicia um loop que continua enquanto a condição for verdadeira.
- `pass`: Indica que nada deve ser feito.
