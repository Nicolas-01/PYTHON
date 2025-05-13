class TipoData:
    dia = 0
    mes = 0
    ano = 0

class TipoProduto:
    codigo = 0
    nome = ''
    data_fabricacao = TipoData()
    data_validade = TipoData()
    preco = 0.0

def menu():
    print('\nSistema para Gerenciar Produtos!')
    print('1 - Cadastrar Produtos\n2 - Visualizar todos os dados\n3 - Sair')
    opcao = int(input('Escolha uma opção: '))
    return opcao

def cadastrar(vet_produto):
    resp = 's'
    while resp == 's':
        print('\nInforme os dados!')
        prod = TipoProduto()
        prod.codigo = int(input('Código: '))
        prod.nome = input('Nome: ')
        prod.preco = float(input('Preço R$: '))
        prod.data_fabricacao = TipoData()
        print('**Data de Fabricação**')
        prod.data_fabricacao.dia = int(input('Dia: '))
        prod.data_fabricacao.mes = int(input('Mês: '))
        prod.data_fabricacao.ano = int(input('Ano: '))
        prod.data_validade = TipoData()
        print('**Data de Validade**')
        prod.data_validade.dia = int(input('Dia: '))
        prod.data_validade.mes = int(input('Mês: '))
        prod.data_validade.ano = int(input('Ano: '))
        vet_produto.append(prod)

        resp = input('\nDeseja cadastrar outro produto?[s/n]: ')
    return vet_produto

def visualizar(vet_prod):
    if len(vet_prod) > 0:
        for i in range(len(vet_prod)):
            print(f'\nCódigo: {vet_prod[i].codigo}\tNome: {vet_prod[i].nome}\tPreco R$: {vet_prod[i].preco}')
            print(f'Data de Fabricação: {vet_prod[i].data_fabricacao.dia}/{vet_prod[i].data_fabricacao.mes}/{vet_prod[i].data_fabricacao.ano}')
            print(f'Data de Validade: {vet_prod[i].data_validade.dia}/{vet_prod[i].data_validade.mes}/{vet_prod[i].data_validade.ano}')
    else:
        print('\nNão há produtos cadastrados!\n')

def main():
    opcao = menu()
    vet_produto = []
    while opcao >= 1 and opcao <= 2:
        if opcao == 1:
            vet_produto = cadastrar(vet_produto)
        elif opcao == 2:
            visualizar(vet_produto)
        opcao = menu()
main()