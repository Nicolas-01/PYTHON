class TipoEndereco:
    rua = ''
    numero = 0
    bairro = ''
    cidade = ''

class TipoFunc:
    codigo = 0
    nome = ''
    endereco = TipoEndereco()
    salario = 0.0

def menu():
    print('\nSistema para Gerenciar Funcionários!')
    print('1 - Cadastrar Funcionário\n2 - Visualizar todos os dados\n3 - Sair')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def cadastrar(vet_func):
    resp = 's'
    while resp == 's':
        func = TipoFunc()
        func.endereco = TipoEndereco()
        print('\nInforme os dados!')
        func.codigo = int(input('Código: '))
        func.nome = input('Nome: ')
        func.endereco.rua = input('Rua: ')
        func.endereco.numero = int(input('Número da casa: '))
        func.endereco.bairro = input('Bairro: ')
        func.endereco.cidade = input('Cidade: ')
        func.salario = float(input('Salário R$: '))
        vet_func.append(func)
        resp = input('\nDeseja cadastrar mais funcionários?[s/n]: ')
    return vet_func

def visualizar(vet_func):
    if len(vet_func) > 0:
        for i in range(len(vet_func)):
            print(f'\nCódigo: {vet_func[i].codigo}\tNome: {vet_func[i].nome}\tSalário: {vet_func[i].salario}')
            print(f'Rua: {vet_func[i].endereco.rua},n° {vet_func[i].endereco.numero}\tBairro: {vet_func[i].endereco.bairro}\tCidade: {vet_func[i].endereco.cidade}')
    else:
        print('\nNão há funcionários cadastrados!\n')
    print()

def main():
    opcao = menu()
    vet_func = []
    while opcao >= 1 and opcao <= 2:
        if opcao == 1:
            vet_func = cadastrar(vet_func)
        elif opcao == 2:
            visualizar(vet_func)
        opcao = menu()
main()