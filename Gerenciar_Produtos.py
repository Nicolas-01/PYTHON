class TipoProd:
    codigo = 0
    nome = ''
    preco = 0.0

def menu():
    print('\nSistema para armazenar informações')
    print('1 - Cadastrar produtos\n2 - Visualizar todos os dados\n3 - Sair')
    opcao = int(input('\nEscolha uma opção: '))
    return opcao

def cadastrar(cont):
    Arquivo_ex2 = open('drive/MyDrive/Classroom/Arquivos/Ex2_Cadastrar_Produtos.txt','w')
    resp = 's'
    print('\n--------------------')
    print(' Cadastrar Produtos')
    print('--------------------')

    while resp == 's':
        if cont <= 10:
            prod = TipoProd()
            prod.codigo = int(input('\nCódigo do Produto: '))
            prod.nome = input('Nome: ')
            prod.preco = float(input('Preço R$: '))
            Arquivo_ex2.write(f'{prod.codigo};{prod.nome};{prod.preco}\n')
            cont += 1
            if cont <= 10:
                resp = input('\nDeseja cadastrar outro Produto?[s/n]: ')
        else:
            print('\n***Número máximo de cadastro atingido!***')
            resp = 'n'
    Arquivo_ex2.close()
    return cont

def visualizar():
    arquivo = open('drive/MyDrive/Classroom/Arquivos/Ex2_Cadastrar_Produtos.txt','r')
    print('\n---------------------------')
    print(' Apresentação dos Produtos')
    print('---------------------------')
    print('\n{:<10}{:<14}{}'.format('Código','Nome','Preço R$'))
    for linha in arquivo.readlines():
        cod,nome,preco = linha.strip().split(';')
        print('{:<10}{:<14}{}'.format(cod,nome,preco))
    arquivo.close()

def main():
    cont = 0
    opcao = menu()
    while opcao >= 1 and opcao <= 2:
        if opcao == 1:
            if cont <= 10:
                cont = cadastrar(cont)
            else:
                print('\n***Número máximo de cadastro atingido!***')
        elif opcao == 2:
            visualizar()
        opcao = menu()
    print('\n-------------------')
    print(' Sistema Encerrado')
    print('-------------------')
main()