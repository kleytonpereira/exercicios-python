agenda = dict()

while True:
    operacao = input('Seleciona uma das opções da agenda. \n1 - adicionar \n2 - buscar \n3 - remover \n4 - listar\n')
    
    if operacao == '1':
        nome = input('Diga o nome do da pessoa que quer adicionar: ')
        
        while True:
            numero = input('Diga o telefone dessa pessoa: ')

            if len(numero) != 8:
                print('Digite um numero valido.')
            else:
                agenda[nome] = numero
                print('Adicionado com sucesso\n')
                break        

    elif operacao == '2':
        nome = input('Diga o nome da pessoa que esta buscando: ')

        print()

        if nome in agenda:
            print(f'Encontramos o numero do(a) {nome}, sendo que é {agenda.get(nome)}\n')
        
    elif operacao == '3':
        nome = input('Diga o nome da pessoa que quer remover: ')
        del agenda[nome]

    elif operacao == '4':
        print(agenda)
    else:
        break
