#Criar um while para inserir "*" entre as letras no nome.

nome = 'Luiz Otávio'
i = 0
novo_nome = ''

while i < len(nome):
    letra = nome[i]
    novo_nome+= f'*{letra}'
    i += 1
novo_nome += '*'
print(novo_nome)