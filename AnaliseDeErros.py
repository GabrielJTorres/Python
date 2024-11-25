"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro."""

Entrada = input("Digite um número inteiro: ")

try:
    numInteiro = int(Entrada)

    if numInteiro % 2 == 0 and numInteiro !=0:
        print(f'O número {numInteiro} é par!')
    elif numInteiro == 0:
        print("O número digitado é zero!")
    else:
        print(f'O número {numInteiro} é ímpar!')

except:    
    print('Por favor digite um número inteiro!')


"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23."""


Entrada = input("Digite a hora atual: ")

if Entrada.isdigit():
    hora = int(Entrada)

    if hora >= 0 and hora <=11:
        print('Bom dia!')
    elif hora > 11 and hora < 18:
        print('Boa tarde!')
    elif hora >=18 and hora < 24:
        print('Boa noite!')
    else:
        print('Este número não é uma hora aceitável')
else:
    print('Digite um número inteiro e positivo!')



"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". """

nome = input('Digite seu nome: ')
tam_nome = len(nome)

if nome.isalpha():
    if tam_nome >2:
        if tam_nome >=2 and tam_nome <=4:
            print('Seu nome é curto.')
        elif tam_nome == 5 or tam_nome == 6:
            print('Seu nome possui um tamanho médio')
        else:
            print('Seu nome é grande!')
    else:
        print('Por favor digite um nome de tamanho aceitável')
else:
    print("Utilize caracteres alfabéticos!")