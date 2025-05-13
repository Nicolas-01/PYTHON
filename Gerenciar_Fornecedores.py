class TipoEnd:
    rua = ''
    bairro = ''
    numero = 0
    cidade = ''

class TipoForn:
    codigo = 0
    nome = ''
    endereco = TipoEnd()

def menu():
    print('\nSistema para armazenar informações')
    print('1 - Cadastrar fornecedores\n2 - Visualizar todos os dados\n3 - Sair')
    opcao = int(input('\nEscolha uma opção: '))
    return opcao

def cadastrar(cont):
    Arquivo_ex1 = open('drive/MyDrive/Classroom/Arquivos/Ex1_Cadastrar_Fornecedor.txt','w')
    resp = 's'
    print('\n----------------------------------')
    print(' Cadastrar dados dos Fornecedores')
    print('----------------------------------')

    while resp == 's':
        if cont <= 10:
            forn = TipoForn()
            forn.endereco = TipoEnd()
            forn.codigo = int(input('\nInforme o código do Fornecedor: '))
            forn.nome = input('Nome do Fornecedor: ')
            print('\n**Endereço**\n')
            forn.endereco.rua = input('Rua: ')
            forn.endereco.numero = int(input('Número: '))
            forn.endereco.bairro = input('Bairro: ')
            forn.endereco.cidade = input('Cidade: ')
            Arquivo_ex1.write(f'{forn.codigo};{forn.nome};{forn.endereco.rua};{forn.endereco.numero};{forn.endereco.bairro};{forn.endereco.cidade}\n')
            cont += 1
            if cont <= 10:
                resp = input('\nDeseja cadastrar outro Fornecedor?[s/n]: ')
        else:
            print('\n***Número máximo de cadastro atingido!***')
            resp = 'n'
    Arquivo_ex1.close()
    return cont

def visualizar():
    arquivo = open('drive/MyDrive/Classroom/Arquivos/Ex1_Cadastrar_Fornecedor.txt','r')
    print('\n-----------------------------------------')
    print(' Apresentação dos dados dos Fornecedores')
    print('-----------------------------------------')
    print('\n{:<10}{:<20}{:<22}{:<12}{:<14}{}'.format('Código','Nome','Rua','Número','Bairro','Cidade'))
    for linha in arquivo.readlines():
        cod,nome,rua,num,bairro,cidade = linha.strip().split(';')
        print('{:<10}{:<20}{:<22}{:<12}{:<14}{}'.format(cod,nome,rua,num,bairro,cidade))
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