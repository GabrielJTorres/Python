from abc import ABC, abstractmethod

# Exercício: Sistema de Gerenciamento de Funcionários

# Classe abstrata (Abstração)
class Funcionario(ABC):  # Abstração: Funcionario é uma classe abstrata que define a estrutura básica para subclasses.
    def __init__(self, nome, salario_base):
        self._nome = nome  # Atributo protegido (Encapsulamento)
        self._salario_base = salario_base  # Atributo protegido (Encapsulamento)

    @abstractmethod
    def calcular_salario(self):  # Método abstrato (Abstração)
        pass

    def exibir_informacoes(self):
        return f"Nome: {self._nome}, Salário: {self.calcular_salario()}"

# Classe derivada (Gerente)
class Gerente(Funcionario):  # Herança: Gerente herda de Funcionario
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)  # Chamada ao construtor da classe base (Herança)
        self._bonus = bonus  # Atributo protegido (Encapsulamento)

    def calcular_salario(self):  # Sobrescrita de método (Polimorfismo)
        return self._salario_base + self._bonus

# Classe derivada (Desenvolvedor)
class Desenvolvedor(Funcionario):  # Herança: Desenvolvedor herda de Funcionario
    def __init__(self, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(nome, salario_base)  # Chamada ao construtor da classe base (Herança)
        self._horas_extras = horas_extras  # Atributo protegido (Encapsulamento)
        self._valor_hora_extra = valor_hora_extra  # Atributo protegido (Encapsulamento)

    def calcular_salario(self):  # Sobrescrita de método (Polimorfismo)
        return self._salario_base + (self._horas_extras * self._valor_hora_extra)

# Classe derivada (Estagiario)
class Estagiario(Funcionario):  # Herança: Estagiario herda de Funcionario
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)  # Chamada ao construtor da classe base (Herança)

    def calcular_salario(self):  # Sobrescrita de método (Polimorfismo)
        return self._salario_base  # Estagiário não tem adicionais

# Menu para entrada de dados
def menu():
    funcionarios = []
    while True:
        print("\nMenu:")
        print("1. Adicionar Gerente")
        print("2. Adicionar Desenvolvedor")
        print("3. Adicionar Estagiário")
        print("4. Exibir Funcionários")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Gerente: ")
            salario_base = float(input("Salário base: "))
            bonus = float(input("Bônus: "))
            funcionarios.append(Gerente(nome, salario_base, bonus))
        elif opcao == "2":
            nome = input("Nome do Desenvolvedor: ")
            salario_base = float(input("Salário base: "))
            horas_extras = int(input("Horas extras: "))
            valor_hora_extra = float(input("Valor por hora extra: "))
            funcionarios.append(Desenvolvedor(nome, salario_base, horas_extras, valor_hora_extra))
        elif opcao == "3":
            nome = input("Nome do Estagiário: ")
            salario_base = float(input("Salário base: "))
            funcionarios.append(Estagiario(nome, salario_base))
        elif opcao == "4":
            print("\nFuncionários:")
            for funcionario in funcionarios:
                print(funcionario.exibir_informacoes())
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()