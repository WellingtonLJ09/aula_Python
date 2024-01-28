#Entrar no sistema de Registro
entrada = input('Você quer "entrar" ou "sair"? ')

#Entrou no sistema e deseja iniciar o cadastro.
if entrada == 'entrar' or entrada =='Entrar' or entrada =='ENTRAR':
    print('Você entrou no sistema ')
    #Código para adicionar os dados do cliente e perguntar se deseja adicionar um novo úsuario e sair
#Deseja sair do sistema.
elif (entrada == 'sair' or entrada =='Sair' or entrada == 'SAIR'):
    print('Você saiu do sistema')
#Opção invalida.
else:
    print('Você não digitou nem entrar e nem sair. ')
