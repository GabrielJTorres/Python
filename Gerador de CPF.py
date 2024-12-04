"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import sys
import re

#Tratando input do usuário com expressão regular
cpf_usuario = input('Insira o seu cpf: ')
cpf = re.sub(r'[^0-9]', '', cpf_usuario)

#Tratando input do usuário em caso de caracteres repetidos
arg_entrada_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
if arg_entrada_sequencial:
    print('Dados repetidos não são CPFs válidos!')
    sys.exit()


cpf_format = cpf[:9]

cont_regressivo_1 = 10

resultado_1 = 0
for unidade in cpf_format:
    resultado_1 += int(unidade) * cont_regressivo_1
    cont_regressivo_1 -= 1
digito_final_1 = (resultado_1 * 10) % 11

digito_final_1 = digito_final_1 if digito_final_1 <= 9 else 0


#Análise do segundo dígito do CPF

cpf_all_digits = cpf_format + str(digito_final_1)
cont_regressivo_2 = 11

resultado_2 = 0
for unidade in cpf_all_digits:
    resultado_2 += int(unidade) * cont_regressivo_2
    cont_regressivo_2 -= 1
digito_final_2 = (resultado_2 * 10) % 11

digito_final_2 = digito_final_2 if digito_final_2 <= 9 else 0


#Confirmando se o cpf é válido

cpf_revisado = f'{cpf_format}{digito_final_1}{digito_final_2}'
if cpf == cpf_revisado:
    print('O CPF',cpf_revisado, 'é válido.')
else:
    print('O CPF',cpf,'não é válido.')