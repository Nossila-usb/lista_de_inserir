# lista de nomes
nomes = []

# inicio do loop
while True:
    # menu
    print('1 - inserir novo nome.')
    print('2 - Exibir lista de nomes.')
    print('3 - ordernar por ordem alfabetica.')
    print('4 - sair do programa.')


    # opcao do usuario
    opcao  = input('Opcao do usuario:')

    # verificacao a opcao escolhida
    match opcao:
        case '1':
            novo_nome = input('insira o novo nome: ')
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
            continue
        case '2':
            print('\nLISTA DE NOMES:\n')
            for nome in nomes:
                print(nome)
            continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('\nLista ordenada com sucesso.')
            continue
        case '4':
            print('Programa encerrado.')
            break
        case _:
            print('opcao invalida')
