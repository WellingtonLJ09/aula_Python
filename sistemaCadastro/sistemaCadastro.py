'''Criar um sistema simples, onde o cliente vai inserir se deseja entrar no sistema para cadastrar
um novo úsuario ou sair. Ao informar que deseja cadastrar um novo úsuario o sistema vai pedir alguns 
dados como nome, CPF, data de nascimento e telefone, quando terminar de inserir os dados
pergunta novamente se deseja adicionar um novo usuario ou sair do sistema.'''

#Inicio no sistema de Registro
decisao = input('Você quer "entrar" ou "sair" no sistema de registro? ')
# Entrou no sistema e deseja iniciar o cadastro.
if decisao.lower().startswith('e'):
  print('Você entrou no sistema ')
  # Código para adicionar os dados do cliente e perguntar se deseja adicionar um novo usuário e sair
  while decisao.lower() != 'sair':
    nome = input('insira o nome: ')
    CPF = input('Insira o número do CPF: ')
    data = input('Insira a data de nascimento: ')
    tel = input('Insira o número de telefone: ')
    decisao = input('Deseja cadastrar um novo usuário ou sair? ')
  print('Você saiu do sistema')
#Deseja sair do sistema.
elif decisao.lower().startswith('s'):
  print('Você saiu do sistema')
#Opção invalida.
else:
  print('Você não digitou nem entrar e nem sair. ')