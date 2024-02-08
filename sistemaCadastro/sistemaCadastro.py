'''Criar um sistema simples, onde o cliente vai inserir se deseja entrar no sistema para cadastrar
um novo úsuario ou sair. Ao informar que deseja cadastrar um novo úsuario o sistema vai pedir alguns 
dados como nome, CPF, data de nascimento e telefone, quando terminar de inserir os dados
pergunta novamente se deseja adicionar um novo usuario ou sair do sistema.'''

#Inicio no sistema de Registro
decisao = input('Você quer "entrar" ou "sair" no sistema de registro? ')
# Entrou no sistema e deseja iniciar o cadastro.
validacao_cpf = 0
validacao_tel = 0
validacao_data = 0
if decisao.lower().startswith('e'):
  print('Você entrou no sistema ')
  # Código para adicionar os dados do cliente e perguntar se deseja adicionar um novo usuário e sair
  while decisao.lower() != 'sair':
    nome = input('insira o nome: ')
    CPF = input('Insira o número do CPF(Apenas numeros): ')
    data = input('Insira a data de nascimento(DDMMAAA): ')
    tel = input('Insira o número de telefone(Apenas o número sem espaços e com DDD): ')
  
    #Validação dos dados digitados
    validacao_valida = None

    try:
      validacao_cpf = int(CPF)
      validacao_data = int(data)
      validacao_tel = int(tel)
      validacao_valida = True
    except:
      validacao = None
    if validacao_valida is None:
      print('Uma das informações estão com informações incorretas.')
      continue

    if len(CPF) > 11 or len(CPF) < 11:
      print('CPF invalido')
      continue

    if len(data) > 8 or len(data) < 8:
      print('Data invalida')
      continue

    if len(tel) > 12 or len(tel) < 11:
      print('Telefone incorreto')
      continue
      #fim da validação
    
    decisao = input('Deseja cadastrar um novo usuário ou sair? ')
  print('Você saiu do sistema')

#Deseja sair do sistema.
elif decisao.lower().startswith('s'):
  print('Você saiu do sistema')
#Opção invalida.
else:
  print('Você não digitou nem entrar e nem sair. ')