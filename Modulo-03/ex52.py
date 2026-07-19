palavra_01 = input('Digite a primeira palavra: ')
palavra_02 = input('Digite a segunda palavra: ')

if sorted(palavra_01) == sorted(palavra_02):
    print(f'A palavra {palavra_01} é um anagrama de {palavra_02}')

resultado_01 = dict()
for x in palavra_01:
    resultado_01[x] = resultado_01.get(x, 0) + 1

resultado_02 = dict()
for x in palavra_02:
    resultado_02[x] = resultado_02.get(x,0) + 1

if resultado_01 == resultado_02:
    print('As palavras são anagramas entre elas')