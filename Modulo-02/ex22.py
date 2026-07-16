nota = []

while True:
    try: 
        entrada = input('Digite as notas: ')
        
        if entrada == 'Interromper' and not nota:
            print('Digite alguma nota')
            continue
        elif entrada == 'Interromper':
            break

        entrada = float(entrada)

        if 10 >= entrada > 0:
            nota.append(entrada)
        else:
            print('Nota invalida')
    except ValueError:
        print('Entrada Invalida')

media = sum(nota) / len(nota)

print (media)