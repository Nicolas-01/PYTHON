class TipoCliente:
    num_max_cliente = 0
    cod_cli = 0
    nome = ''
    fone = ''

class TipoDocumento:
    num_doc = 0
    num_max_doc_por_cliente = 0
    cod_cli = 0
    dia_venc = 0
    dia_pag = 0
    valor = 0.0
    juros = 0.0
    valor_total = 0.0

def menu():
    print('\n\tSistema de Gerenciamento de Documentos e Clientes')
    print('-'*98)
    print('{:<37}|  {}'.format(' 1 - Cadastrar clientes','6 - Excluir documentos individuais pelo número'))
    print('{:<37}|  {}'.format(' 2 - Relatório de clientes','7 - Excluir documentos por cliente'))
    print('{:<37}|  {}'.format(' 3 - Cadastrar documentos','8 - Excluir documentos por período'))
    print('{:<37}|  {}'.format(' 4 - Relatório de documentos','9 - Alterar as informações dos clientes'))
    print('{:<37}|  {}'.format(' 5 - Excluir clientes sem documentos','10 - Mostrar o total de documentos de determinado cliente'))
    print('-'*98)
    opcao = int(input('\nQual opção deseja?: '))
    return opcao

def cadastrar_cliente(vet_cliente,numero_max_cliente):
    resp = 's'
    print('\n---------------------------')
    print(' Cadastramento de Clientes')
    print('---------------------------')
    while resp == 's':
        if numero_max_cliente < 15:
            cont = 0
            cliente = TipoCliente()
            print('\nInforme os dados!')
            cliente.cod_cli = int(input('Código do Cliente: '))
            if len(vet_cliente) > 0:
                for i in range(len(vet_cliente)):
                    if cliente.cod_cli == vet_cliente[i].cod_cli:
                        print('\n**Código já cadastrado!**\n')
                        cont += 1
                if cont == 0:
                    cliente.nome = input('Nome e Sobrenome: ').upper()
                    cliente.fone = int(input('Telefone: '))
                    cliente.num_max_cliente += 1
                    vet_cliente.append(cliente)
                    numero_max_cliente += 1
            else:
                cliente.nome = input('Nome: ').upper()
                cliente.fone = int(input('Telefone: '))
                cliente.num_max_cliente += 1
                vet_cliente.append(cliente)
                numero_max_cliente += 1
            if numero_max_cliente < 15:
                resp = input('Deseja cadastrar outra pessoa?[s/n]: ')
        else:
            print('\n**Limite de clientes atingido!**')
            resp = 'n'
    return vet_cliente,numero_max_cliente

def relatorio_cliente(vet_cliente):
    print('\n**Relatório de Clientes**')
    if len(vet_cliente) > 0:
        print('\n{:<11}{:<26}{}'.format('Código','Nome','Telefone'))
        for i in range(len(vet_cliente)):
            print('{:<11}{:<26}{}'.format(vet_cliente[i].cod_cli,vet_cliente[i].nome,vet_cliente[i].fone))
    else:
        print('\nNão há clientes cadastrados!')

def cadastrar_doc(vet_doc,cliente,num_max_doc):
    print('\n-----------------------------')
    print(' Cadastramento de Documentos')
    print('-----------------------------')
    if len(cliente) > 0:
        resp = 's'
        while resp == 's':
            if num_max_doc < 15:
                cont = 0
                cont2 = 0
                codigo_cliente = int(input('\nInforme o CÓDIGO do cliente: '))
                for i in range(len(vet_doc)):
                    if codigo_cliente == vet_doc[i].cod_cli:
                        print('\nCliente já cadastrado!')
                        cont += 1
                if cont == 0:
                    for i in range(len(cliente)):
                        if codigo_cliente == cliente[i].cod_cli:
                            print(f'Cliente: {cliente[i].nome}')
                            doc = TipoDocumento()
                            doc.num_doc = int(input('Número do Documento: '))
                            doc.cod_cli = codigo_cliente
                            doc.dia_pag = int(input('Dia do pagamento: '))
                            doc.dia_venc = int(input('Dia do vencimento: '))
                            doc.valor = float(input('Valor R$: '))
                            if doc.dia_pag > doc.dia_venc:
                                doc.juros = doc.valor * 0.05
                                print(f'Juros por atraso no pagamento R$: {doc.juros}')
                                print(f'Valor total R$: {doc.valor + doc.juros}')
                            doc.valor_total = doc.valor + doc.juros
                            doc.num_max_doc_por_cliente += 1
                            cont2 += 1
                            vet_doc.append(doc)
                            num_max_doc += 1
                    if cont2 == 0:
                        print('\n**Código Inválido!**')
                if num_max_doc < 15:
                    resp = input('\nDeseja cadastrar outro documento?[s/n]: ')
            else:
                print('\n**Limite de documentos por cliente atingido!**')
                resp = 'n'
    else:
        print('\nNão há clientes cadastrados!')
    return vet_doc,cliente,num_max_doc

def relatorio_doc(vet_doc):
    print('\n-------------------------')
    print(' Relatório de Documentos')
    print('-------------------------')
    if len(vet_doc) > 0:
        print('\n{:<11}{:<16}{:<20}{:<20}{}'.format('Código','N° Documento','Dia de Pagamento','Dia de Vencimento','Valor R$'))
        for i in range(len(vet_doc)):
            print('{:<11}{:<16}{:<20}{:<20}{:.2f}'.format(vet_doc[i].cod_cli,vet_doc[i].num_doc,vet_doc[i].dia_pag,vet_doc[i].dia_venc,vet_doc[i].valor_total))
    else:
        print('\nNão há documentos cadastrados!')

def excluir_cliente_sem_doc(vet_cliente,vet_doc):
    print('\n-------------------------------------')
    print(' Exclusão de Clientes sem Documentos')
    print('-------------------------------------')
    cont = 0
    if len(vet_cliente) > 0:
        codigo_cliente = int(input('\nInforme o CÓDIGO do cliente que deseja excluir: '))
        for i in range(len(vet_cliente)):
            for j in range(len(vet_doc)):
                if codigo_cliente == vet_doc[j].cod_cli:
                    cont += 1
            if cont >  0:
                print('\nCliente possui documentos cadastrados!')
            else:
                if codigo_cliente == vet_cliente[i].cod_cli:
                    vet_cliente.pop(i)
                    print('\nCliente excluído com sucesso!')
                else:
                    print('\nCliente não encontrado!')
    else:
        print('\nNão há clientes cadastrados!')
    return vet_cliente,vet_doc

def excluir_doc_por_num(vet_doc):
    print('\n-----------------------------------')
    print(' Exclusão de Documentos por número')
    print('-----------------------------------')
    if len(vet_doc) > 0:
        num_doc = int(input('\ninforme o NÚMERO do documento que deseja excluir: '))
        for i in range(len(vet_doc)):
            if num_doc == vet_doc[i].num_doc:
                vet_doc.pop(i)
                print('\nDocumentos Excluidos!')
            else:
                print('\nDocumento não encontrado!')
    else:
        print('\nNão há documentos cadastrados!\n')
    return vet_doc

def excluir_doc_cliente(vet_doc):
    # excluir documento de cliente por código
    print('\n----------------------------------------------')
    print(' Exclusão de Documentos por Código do Cliente')
    print('----------------------------------------------')
    cont = 0
    if len(vet_doc) > 0:
        cod_cliente = int(input('\nInforme o CÓDIGO do cliente que deseja excluir os documentos: '))
        for i in range(len(vet_doc)):
            if cod_cliente == vet_doc[i].cod_cli:
                vet_doc.pop(i)
                print('Documentos excluídos!')
                cont += 1
        if cont == 0:
            print('\nCliente não encontrado!')
    else:
        print('\nNão há documentos cadastrados!')
    return vet_doc

def excluir_doc_periodo(vet_doc):
    if len(vet_doc) > 0:
        cont = 0
        print('\n------------------------------------')
        print(' Exclusão de Documentos por Período')
        print('------------------------------------')
        print('Por exemplo, os documentos que possuem data de vencimento do dia 12 ao dia 15 serão excluídos!')
        dia_inicial = int(input('\nDo dia: '))
        dia_final = int(input('Até o dia: '))
        for i in range(len(vet_doc)):
            if dia_inicial <= vet_doc[i].dia_venc <= dia_final:
                vet_doc.pop(i)
                print('\nDocumentos excluídos!')
                cont += 1
        if cont == 0:
            print('\nNão há documentos cadastrados nesse período!')
    else:
        print('\nNão há documentos cadastrados!')
    return vet_doc

def alterar_dados(vet_cliente,vet_doc):
    print('\n--------------------')
    print(' Alteração de Dados')
    print('--------------------')
    if len(vet_cliente) > 0:
        resp = 's'
        while resp == 's':
            print('\nO que deseja alterar?')
            print('1 - Nome\n2 - Telefone\n3 - Número do documento\n4 - Dia do Pagamento\n5 - Dia do Vencimento\n6 - Valor')
            escolha = int(input('Qual opção deseja?: '))
            codigo = int(input('\nInforme o CÓDIGO do cliente que deseja fazer alteração: '))
            cont1 = 0
            cont2 = 0
            cont3 = 0
            cont4 = 0
            cont5 = 0
            cont6 = 0

            if escolha == 1:
                for i in range(len(vet_cliente)):
                    if codigo == vet_cliente[i].cod_cli:
                        nome_novo = input('\nInforme o novo nome: ').upper()
                        vet_cliente[i].nome = nome_novo
                        print('\nNome alterado com sucesso!')
                        cont1 += 1
                if cont1 == 0:
                    print('\nCódigo Inválido!')

            elif escolha == 2:
                for i in range(len(vet_cliente)):
                    if codigo == vet_cliente[i].cod_cli:
                        telefone_novo = int(input('\nInforme o novo telefone: '))
                        vet_cliente[i].fone = telefone_novo
                        print('\nTelefone alterado com sucesso!')
                        cont2 += 1
                if cont2 == 0:
                    print('\nCódigo Inválido!')

            elif escolha == 3:
                for i in range(len(vet_doc)):
                    if codigo == vet_cliente[i].cod_cli:
                        novo_num_doc = int(input('\nInforme o novo número do documento: '))
                        vet_doc[i].num_doc = novo_num_doc
                        print('\nNúmero do documento alterado com sucesso!')
                        cont3 += 1
                if cont3 == 0:
                    print('\nCódigo Inválido!')

            elif escolha == 4:
                for i in range(len(vet_doc)):
                    if codigo == vet_cliente[i].cod_cli:
                        novo_dia_pag = int(input('\nInforme o novo dia de pagamento: '))
                        vet_doc[i].dia_pag = novo_dia_pag
                        if vet_doc[i].dia_pag <= vet_doc[i].dia_venc:
                            desconto_valor = vet_doc[i].valor * 0.05
                            novo_valor = vet_doc[i].valor_total - desconto_valor
                            print(f'\nVocê recebeu R$ {desconto_valor:.2f} de volta.')
                            vet_doc[i].valor_total = novo_valor
                        print('\nDia de pagamento alterado com sucesso!')
                        cont4 += 1
                if cont4 == 0:
                    print('\nCódigo Inválido!')

                elif escolha == 5:
                    for i in range(len(vet_doc)):
                        if codigo == vet_cliente[i].cod_cli:
                            novo_dia_venc = int(input('\nInforme o novo dia de vencimento: '))
                            vet_doc[i].dia_venc = novo_dia_venc
                            if vet_doc[i].dia_pag > vet_doc[i].dia_venc:
                                acrescentar_valor = vet_doc[i].valor * 0.05
                                novo_valor = vet_doc[i].valor_total + acrescentar_valor
                                print(f'\nVocê pagará R$ {acrescentar_valor:.2f} de juros por ultrapassar o dia de pagamento.')
                                vet_doc[i].valor_total = novo_valor
                            print('\nDia de vencimento alterado com sucesso!')
                            cont5 += 1
                if cont5 == 0:
                    print('\nCódigo Inválido!')

                elif escolha == 6:
                    for i in range(len(vet_doc)):
                        if codigo == vet_doc[i].cod_cli:
                            novo_valor = float(input('\nInforme o novo valor: '))
                            vet_doc[i].valor_total = novo_valor
                            print('\nValor alterado com sucesso!')
                            cont6 += 1
                if cont6 == 0:
                    print('\nCódigo Inválido!')
            resp = input('\nDeseja fazer outra alteração?[s/n]: ')
    else:
        print('Não há clientes cadastrados!')
    return vet_cliente,vet_doc

def total_doc(vet_doc,vet_cliente):
    resp = 's'
    if len(vet_cliente) > 0:
        print('\n---------------------------------')
        print(' Total de documentos por cliente')
        print('---------------------------------')
        while resp == 's':
            codigo_cliente = int(input('\nInforme o CÓDIGO do cliente: '))
            cont = 0
            for cliente in vet_cliente:
                soma = 0
                soma += cliente.num_max_cliente
                if codigo_cliente == cliente.cod_cli:
                    cont += 1
                    for doc in vet_doc:
                        if doc.cod_cli == codigo_cliente:
                            soma += doc.num_max_doc_por_cliente
                    print('\n{:<25}{}'.format('Nome','N° Documentos'))
                    print('{:<25}{}'.format(cliente.nome,soma))
            if cont == 0:
                print('\nCliente não encontrado!')
            resp = input('\nDeseja visualizar novamente?[s/n]: ')
    else:
        print('\nNão há documentos cadastrados!')

def main():
    opcao = menu()
    vet_cliente = []
    vet_doc = []
    num_max_cliente = 0
    num_max_doc_por_cliente = 0

    while opcao >= 1 and opcao <= 10:
        if opcao == 1:
            if num_max_cliente < 15:
                vet_cliente,num_max_cliente = cadastrar_cliente(vet_cliente,num_max_cliente)
            else:
                print('\n**Limite de clientes atingido!**')
        elif opcao == 2:
            relatorio_cliente(vet_cliente)
        elif opcao == 3:
            if num_max_doc_por_cliente < 15:
                vet_doc,vet_cliente,num_max_doc_por_cliente = cadastrar_doc(vet_doc,vet_cliente,num_max_doc_por_cliente)
            else:
             print('\n**Limite de documentos por cliente atingido!**')
        elif opcao == 4:
            relatorio_doc(vet_doc)
        elif opcao == 5:
            vet_cliente,vet_doc = excluir_cliente_sem_doc(vet_cliente,vet_doc)
        elif opcao == 6:
            vet_doc = excluir_doc_por_num(vet_doc)
        elif opcao == 7:
            vet_doc = excluir_doc_cliente(vet_doc)
        elif opcao == 8:
            vet_doc = excluir_doc_periodo(vet_doc)
        elif opcao == 9:
            vet_cliente,vet_doc = alterar_dados(vet_cliente,vet_doc)
        elif opcao == 10:
            total_doc(vet_doc,vet_cliente)
        opcao = menu()
main()