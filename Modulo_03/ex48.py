resultado = dict()

while True:
    nome = input('Diga o nome do aluno (Caso queira acabar, digite "1 - Encerrar)": ')
    notas = []

    if nome == '1 - Encerrar':
        break
    
    while True:
        entrada = input('Diga as notas desse aluno (Caso acabe as notas desse aluno digite "2 - Finalizar"): ')

        if entrada == '2 - Finalizar':
            break
            
        notas.append(int(entrada))

    resultado[nome] = notas

for x in resultado.items():
    if 7 <= sum(x[1]) / len(x[1]):
        print(f'O {x[0]} passou com a media {sum(x[1]) / len(x[1])}')
    else:
        print(f'O {x[0]} não passou com a media {sum(x[1]) / len(x[1])}')

print(resultado)