"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número: ')
if num.isdigit():
  print('número inteiro')
  if (int(num) % 2) == 0:
    print('número par')
  else:
    print('Número impar')
else:
  print('Número não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Digite a hora: '))
if (hora >= 0) and (hora <= 11):
    print('Bom Dia')
if(hora >= 12) and (hora <= 17):
    print('Boa Tarde')
if(hora >= 18) and (hora <= 23):
    print('Boa noite')

    #RESPOSTA PROFESSOR:
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite o seu nome: ")

nomeP = len(nome)
if nomeP >1:
    if nomeP <=4:
        print('Seu nome é curto')
    elif (nomeP >= 5) and (nomeP <= 6):
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')