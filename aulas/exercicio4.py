#Contar letras da frase e descobrir qual letra que mais vezes se repetiu.

frase = 'O Python é uma lingaguem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum. '

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letral_atual = frase[i]

    if letral_atual == ' ':
        i+=1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letral_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_que_apareceu_mais_vezes = letral_atual
    i+=1

print(f'A letra que apareceu mais vezes foi {letra_que_apareceu_mais_vezes} que apaeceu {qtd_apareceu_mais_vezes}x')