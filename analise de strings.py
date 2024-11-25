nome = input('Digite seu nome:')
idade = input('Informe quantos anos você tem: ')

try:
    idade = int(idade)

    if nome and idade:
        print(f'Olá {nome}! Você possui {idade} anos de idade.' )
        print(f'Seu nome invertido fica assim: {nome[::-1]}')

        #condição pra verificar se contem espaços ou não
        if ' ' in nome:
            print('Seu nome contém espaços.')
        else:
            print('Seu nome NÃO contém espaços.')

        #fim da condição dos espaços

        print(f'Seu nome contém {len(nome)} letras.')
        print(f'A primeira letra do seu nome é: "{nome[0]}"')
        print(f'A última letra do seu nome é: "{nome[-1]}"')
    else:
        print('Preencha corretamente os campos de nome e idade!')
except:
    print('O campo de idade deve ser preenchido com um número!')
        