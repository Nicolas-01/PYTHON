class TipoBanco:
  numero_conta = 0
  nome = ''
  saldo = 0.0

def menu():
  print('\n**Sistema de Gerenciamento de Banco**')
  print('1. Cadastrar contas\n2. Visualizar todas as contas\n3. Consultar por Nome\n4. Alterar nome e/ou saldo de um número de conta')
  print('5. Excluir a conta com menor saldo\n6. Sair')
  opcao = int(input('Escolha uma opção: '))
  return opcao

def cadastrar(vet_conta):
  resp = 's'
  while resp == 's':
    conta = TipoBanco()
    conta.numero_conta = int(input('\nInforme o número da conta: '))
    conta.nome = input('Nome do titular da conta: ')
    conta.saldo = float(input('Saldo R$: '))
    vet_conta.append(conta)
    resp = input('Deseja cadastrar outra pessoa?[s/n]: ').lower()
  return vet_conta

def visualizar(vet_conta):
  if len(vet_conta) > 0:
    for i in range(len(vet_conta)):
      print('\nConta: ',vet_conta[i].numero_conta,'\tNome: ',vet_conta[i].nome,'\tSaldo R$: ',vet_conta[i].saldo)
  else:
    print()
    print('*'*27)
    print('\nNão há pessoas cadastradas!\n')
    print('*'*27)

def consultar(vet_conta):
  cont = 0
  if len(vet_conta) > 0:
    nome_pesquisa = input('\nQual nome deseja pesquisar?: ')
    for i in range(len(vet_conta)):
      if nome_pesquisa == vet_conta[i].nome:
        print('\nConta: ',vet_conta[i].numero_conta,'\tNome: ',vet_conta[i].nome,'\tSaldo R$: ',vet_conta[i].saldo)
        cont += 1
    if cont < 1:
      print('\nNome não encontrado!')
  else:
    print()
    print('*'*27)
    print('\nNão há pessoas cadastradas!\n')
    print('*'*27)

def alterar(vet_conta):
  if len(vet_conta) > 0:
    conta = int(input('\nDigite o NÚMERO DA CONTA para alterar o "SALDO" ou "NOME": '))
    for i in range(len(vet_conta)):
      if conta == vet_conta[i].numero_conta:
        escolha = input('Digite "N" para alterar o nome ou "S" para saldo!: ').lower()
        if escolha == 'n':
              vet_conta[i].nome = input('\nNovo nome: ')
              print('Alteração realizada!')

        elif escolha == 's':
          vet_conta[i].saldo = float(input('\nNovo saldo R$: '))
          print('Alteração realizada!')
  else:
    print()
    print('*'*27)
    print('\nNão há pessoas cadastradas!\n')
    print('*'*27)
  return vet_conta

def excluir(vet_conta):
  if len(vet_conta) > 0:
    for i in range(len(vet_conta)):
      if i == 0:
        menor_saldo = vet_conta[i].saldo
        indice = i
      else:
        if vet_conta[i].saldo < menor_saldo:
          menor_saldo = vet_conta[i].saldo
          indice = i
    vet_conta.pop(indice)
    print()
    print('*'*31)
    print('\nExclusão realizada com sucesso!\n')
    print('*'*31)

  else:
    print()
    print('*'*27)
    print('\nNão há pessoas cadastradas!\n')
    print('*'*27)
  return vet_conta

def main():
  vet_conta = []
  opcao = menu()

  while opcao >= 1 and opcao <= 5:
    if opcao == 1:
      vet_conta = cadastrar(vet_conta)
    elif opcao == 2:
      visualizar(vet_conta)
    elif opcao == 3:
      consultar(vet_conta)
    elif opcao == 4:
      vet_conta = alterar(vet_conta)
    elif opcao == 5:
      vet_conta = excluir(vet_conta)
    opcao = menu()
    
main()