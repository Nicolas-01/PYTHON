class TipoAluno:
    matricula = 0
    nome = ''
    telefone = 0

def menu():
    print('\nSistema para armazenar informações')
    print('1 - Cadastrar alunos\n2 - Visualizar todos os dados\n3 - Sair')
    opcao = int(input('\nEscolha uma opção: '))
    return opcao

def cadastrar(cont):
    Arquivo_ex3 = open('drive/MyDrive/Classroom/Arquivos/Ex3_Cadastrar_Alunos.txt','w')
    resp = 's'
    print('\n------------------')
    print(' Cadastrar Alunos')
    print('------------------')

    while resp == 's':
        if cont <= 10:
            aluno = TipoAluno()
            aluno.matricula = int(input('\nMatrícula: '))
            aluno.nome = input('Nome: ')
            aluno.telefone = int(input('Telefone: '))
            Arquivo_ex3.write(f'{aluno.matricula};{aluno.nome};{aluno.telefone}\n')
            cont += 1
            if cont <= 10:
                resp = input('\nDeseja cadastrar outro Aluno?[s/n]: ')
        else:
            print('\n***Número máximo de cadastro atingido!***')
            resp = 'n'
    Arquivo_ex3.close()
    return cont

def visualizar():
    arquivo = open('drive/MyDrive/Classroom/Arquivos/Ex3_Cadastrar_Alunos.txt','r')
    print('\n-------------------------')
    print(' Apresentação dos Alunos')
    print('-------------------------')
    print('\n{:<13}{:<19}{}'.format('Matrícula','Nome','Telefone'))
    for linha in arquivo.readlines():
        mat,nome,tel = linha.strip().split(';')
        print('{:<13}{:<19}{}'.format(mat,nome,tel))
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