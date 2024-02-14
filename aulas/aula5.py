"""
Sistema com limite de tentativa de senhas para treinar o FOR(Usada quando sabemos a quantidade de repetições
definida, diferente do WHILE que deve ser usada quando não sabemos a quantidade de repetições.)
FOR = Para...de...até..passo...faça
WHILE = Enquanto
"""

senha_correta = "senha123"
tentativas_maximas = 4

#Range = foi usado para saber quando parar o laço de repetição.
for tentativa in range(tentativas_maximas):
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tentativa", tentativa + 1, "de", tentativas_maximas)

if senha_digitada != senha_correta:
    print("Número máximo de tentativas excedido. Acesso bloqueado.")
