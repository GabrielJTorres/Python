# Simulação de Biblioteca com POO em Python:
'''
Crie um sistema em Python que simule uma biblioteca. O sistema deve utilizar os conceitos de Herança, Polimorfismo, Abstração e Encapsulamento. Siga as instruções abaixo:

1. Crie uma classe abstrata chamada `ItemBiblioteca` que possua os atributos encapsulados `titulo` e `autor`, além de um método abstrato chamado `exibir_informacoes`.

2. Implemente duas classes concretas que herdam de `ItemBiblioteca`: `Livro` e `Revista`. Cada uma deve implementar o método `exibir_informacoes` de forma polimórfica,
exibindo as informações específicas de cada tipo de item.

3. Adicione um atributo exclusivo para cada classe concreta:
    - `Livro`: número de páginas.
    - `Revista`: edição.

4. Crie uma classe chamada `Biblioteca` que encapsule uma lista de itens da biblioteca. Essa classe deve ter métodos para:
    - Adicionar um item à biblioteca.
    - Listar todos os itens, exibindo suas informações.

5. No programa principal, crie um menu para que o usuário insira instâncias de `Livro` e `Revista`, adicione-as à biblioteca e exiba as informações de todos os itens.

Certifique-se de aplicar corretamente os conceitos de Herança, Polimorfismo, Abstração e Encapsulamento no código.

'''

from abc import ABC, abstractmethod

# Criação de Classes

# Classe abstrata base para itens da biblioteca
class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
    
    @abstractmethod
    def exibir_informacoes(self):
        pass

# Classe para representar um Livro, herda de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self._paginas = paginas
        
    def exibir_informacoes(self):
        return f'Titulo: {self._titulo}, Autor: {self._autor}, Número de Páginas: {self._paginas}.'

# Classe para representar uma Revista, herda de ItemBiblioteca
class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, editora):
        super().__init__(titulo, autor)
        self._editora = editora
            
    def exibir_informacoes(self):
        return f'Titulo: {self._titulo}, Autor: {self._autor}, Editora: {self._editora}.'

# Classe Biblioteca para gerenciar itens
class Biblioteca:
    def __init__(self):
        self._itens = []
    
    # Adiciona um item à biblioteca, verificando se é do tipo correto
    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
        else:
            raise TypeError('O item deve ser uma instância de "ItemBiblioteca."')
        
    # Lista todos os itens da biblioteca
    def listar_itens(self):
        if not self._itens:
            print('A biblioteca está vazia')
        else:
            for item in self._itens:
                print(item.exibir_informacoes())

# Programa principal

# Função para exibir o menu e interagir com o usuário
def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Adicionar Revista")
        print("3. Listar Itens")
        print("4. Sair")
        opcao = input('Insira o número de alguma opção: ')
        
        if opcao == '1':
            # Adiciona um livro à biblioteca
            titulo = input('Título: ')
            autor = input('Autor: ')
            paginas = input('Número de páginas: ')
            livro = Livro(titulo, autor, paginas)
            biblioteca.adicionar_item(livro)
            print('Livro adicionado com sucesso.')
            
        elif opcao == '2':
            # Adiciona uma revista à biblioteca
            titulo = input('Título: ')
            autor = input('Autor: ')
            editora = input('Editora: ')
            revista = Revista(titulo, autor, editora)
            biblioteca.adicionar_item(revista)
            print('Revista adicionada com sucesso.')
            
        elif opcao == "3":
            # Lista os itens da biblioteca
            print("\nItens na Biblioteca:")
            if not biblioteca._itens:
                print("A biblioteca está vazia.")
            else:
                for item in biblioteca._itens:
                    if isinstance(item, Livro):
                        print(f"[Livro] {item.exibir_informacoes()}")
                    elif isinstance(item, Revista):
                        print(f"[Revista] {item.exibir_informacoes()}")
  
        elif opcao == '4':
            # Sai do programa
            print('Saindo do programa...')
            break
        
        else:
            # Trata opções inválidas
            print('Opcão inválida.')
            
# Ponto de entrada do programa
if __name__ == '__main__':
    menu()