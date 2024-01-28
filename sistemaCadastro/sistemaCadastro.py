#Entrar no sistema de Registro
entrada = input('Você quer "entrar" ou "sair"? ')

#Entrou no sistema e deseja iniciar o cadastro.
if entrada == 'entrar' or 'Entrar' or 'ENTRAR':
    print('Você entrou no sistema ')
    #Código para adicionar os dados do cliente e perguntar se deseja adicionar um novo úsuario e sair
#Deseja sair do sistema.
elif entrada == 'sair' or 'Sair' or 'SAIR':
    print('Você saiu do sistema')
#Opção invalida.
else:
    print('Você não digitou nem entrar e nem sair. ')
