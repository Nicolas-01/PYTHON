class TipoAluno:
  nome = ''
  dia_nascimento = 0
  mes_nascimento = 0
  ano_nascimento = 0
  telefone = 0
  rua_endereco = ''
  numero_endereco = 0
  bairro_endereco = 0
  serie = 0

def menu():
  print('\n**Sistemas para Gerenciar alunos da escola**')
  print('1. Cadastrar alunos\n2. Consultar por nome\n3. Visualizar todos os dados\n4. Sair')
  opcao = int(input('Escolha uma opção: '))
  return opcao

def cadastrar(vet_aluno):
  resp = 's'
  while resp == 's' and len(vet_aluno) <= 500:
    aluno = TipoAluno()
    aluno.nome = input('\nNome: ')
    aluno.dia_nascimento = int(input('** Data de Nascimento **\nDia: '))
    aluno.mes_nascimento = int(input('Mês: '))
    aluno.ano_nascimento = int(input('Ano: '))
    aluno.serie = int(input('Série: '))
    aluno.telefone = int(input('Telefone: '))
    aluno.rua_endereco = input('** Endereço **\nRua: ')
    aluno.numero_endereco = int(input('Número: '))
    aluno.bairro_endereco = input('Bairro: ')
    vet_aluno.append(aluno)
    resp = input('Deseja cadastrar mais alunos?[s/n]: ').lower()
  return vet_aluno

def consultar(vet_a):
    cont = 0
    if len(vet_a) > 0:
        nome_pesquisa = input('\nQual aluno deseja pesquisar?:  ')
        for i in range(len(vet_a)):
            if nome_pesquisa == vet_a[i].nome:
              print(f'\nNome: {vet_a[i].nome}\tData de Nascimento: {vet_a[i].dia_nascimento}/{vet_a[i].mes_nascimento}/{vet_a[i].ano_nascimento}\tTelefone: {vet_a[i].telefone}\tSérie: {vet_a[i].serie}')
              print(f'Rua: {vet_a[i].rua_endereco},n° {vet_a[i].numero_endereco}\tBairro: {vet_a[i].bairro_endereco}')
              cont += 1
            if cont < 1:
              print('\n**Aluno não encontrado!**')
    else:
        print('\n**Não há alunos cadastros!**')

def visualizar(vet_a):
  if len(vet_a) > 0:
    for i in range(len(vet_a)):
      print(f'\nNome: {vet_a[i].nome}\tData de Nascimento: {vet_a[i].dia_nascimento}/{vet_a[i].mes_nascimento}/{vet_a[i].ano_nascimento}\tTelefone: {vet_a[i].telefone}\tSérie: {vet_a[i].serie}')
      print(f'Rua: {vet_a[i].rua_endereco},n° {vet_a[i].numero_endereco}\tBairro: {vet_a[i].bairro_endereco}')
  else:
    print('\n**Não há alunos cadastrados!**')

def main():
  vet_alunos = []
  opcao = menu()
  while opcao >= 1 and opcao <= 3:
    if opcao == 1:
      if len(vet_alunos) <= 500:
        vet_alunos = cadastrar(vet_alunos)
      else:
        print('\nCapacidade máxima atingida !!!')
    elif opcao == 2:
      consultar(vet_alunos)
    elif opcao == 3:
      visualizar(vet_alunos)
    opcao = menu()

main()
