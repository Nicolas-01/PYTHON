print(' *'*26,'\n Programa para Gerenciamento de Estoque de Produtos\n','* '*26)
print()
nome = []
qtd = []
preco = []

def cadastro():
  print('Cadastro de produto!')
  continuar = 's'

  while continuar == 's':
      nome.append(input(f'\nInforme o nome do produto: '))
      qtd.append(int(input('Quantidade do produto: ')))
      preco.append(float(input(f'Valor: R$ ')))
      continuar = input('Continuar cadastro? [S/N]: ').lower()

  print('\n')
  main()

def apresentacao():
  print('{:<20}{:<18}{:<10}'.format('Nome','Quantidade','Preço R$'))
  for i in range(len(nome)):
    print('{:<20}\t{:<15}\t{:.2f}\t'.format(nome[i],qtd[i],preco[i]))

  print('\n')
  main()

def estoque_minimo():
  cont = 0
  print()
  for i in range(len(qtd)):
    if qtd[i] <= 3:
      print(f'O produto {nome[i]} está com o estoque mínimo: {qtd[i]}')
      cont += 1

  if cont == 0:
    print('Nenhum produto tem estoque mínimo!')
  print('\n')
  main()

def aumento():
  for i in range(len(preco)):
    if nome[i].startswith('c') or nome[i].startswith('C'):
      preco[i] = preco[i] + (preco[i] * 5 / 100)
      print(f'\nReajuste aplicado com sucesso!\nNovo preço do produto: {nome[i]} R$ {preco[i]:.2f}')

  print('\n')
  main()

def alterar_nome():
  nome_trocar = input('\nNome do produto que deseja trocar: ')
  nome_novo = input('Novo nome: ')

  for i in range(len(nome)):
    if nome_trocar in nome[i]:
      nome[i] = nome[i].replace(nome_trocar, nome_novo)
  print('Nome alterado!')
  print('\n')
  main()

def capitalizar_nomes():
  for i in range(len(nome)):
    nome[i] = nome[i].capitalize()

  print('Capitalizado com sucesso!')
  print('\n')
  main()

def main():
  if len(nome) == 0:
    cadastro()

  else:
    print('1 - Cadastro: nome, quantidade e preço\n2 - Apresentar todos os produtos')
    print('3 - Apresentar estoque mínimo\n4 - Reajuste de aumento em 5% dos produtos que começam com a letra "C"')
    print('5 - Alterar nome do produto\n6 - Capitalizar nome dos produto\n7 - Sair')
    escolha = int(input('\nEscolha uma opcão: '))

    if escolha == 1:
      cadastro()

    elif escolha == 2:
      apresentacao()

    elif escolha == 3:
      estoque_minimo()

    elif escolha == 4:
      aumento()

    elif escolha == 5:
      alterar_nome()

    elif escolha == 6:
      capitalizar_nomes()

    if escolha < 1 or escolha > 6:
      print('GERENCIADOR ENCERRADO!!!')

main()