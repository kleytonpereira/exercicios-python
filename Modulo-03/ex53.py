palavra = input('Digite a palavra: ')

palavra_nova = ''

palavra_nova = palavra_nova.join((chr(((ord(x)- 97) + 2) % 26 + 97) for x in palavra)) 

print(palavra_nova)