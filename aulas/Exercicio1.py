'''
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada fpr digitado em nome ou idade:
    exiba. "Desculpa, você deixou campos vazios."
'''

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é', nome[::-1])
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print("Seu nome tem %d letras" %len(nome))
    print(f'A primeira letra do seu nome é: ', nome[:1:])
    print(f'A ultima letra do seu nome é: ', nome[-1::])
else:
    print('Desculpa, você deixou campos vazios.')