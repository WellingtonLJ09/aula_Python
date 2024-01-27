#Entrar no sistema de Registro
entrada = input('Você quer "entrar" ou "sair"? ')

#Entrou no sistema e deseja iniciar o cadastro.
if entrada == 'entrar' or 'Entrar' or 'ENTRAR':
    print('Você entrou no sistema ')
#Deseja sair do sistema.
elif entrada == 'sair' or 'Sair' or 'SAIR':
    print('Você saiu do sistema')
#Opção invalida.
else:
    print('Você não digitou nem entrar e nem sair. ')
