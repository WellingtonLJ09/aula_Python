'''
REPETIÇÕES

While(enquanto)
Executa uma ação enquanto uma condição for verdadeira
'''
numero = input('Digite o número que você deseja saber a tabuada: ')
numero = int(numero)
i = 0

while i <= 10:
    soma = numero + i
    print(f'{i} + {numero} = {soma}')
    i += 1
    

print("fim da conta")

