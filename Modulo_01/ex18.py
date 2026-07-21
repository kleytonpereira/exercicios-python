valor = int(input())

cem = valor // 100
valor_sobrando = valor - cem * 100
cinquenta = valor_sobrando % 100 // 50
valor_sobrando -= cinquenta * 50
vinte = (valor_sobrando % 100) % 50 // 20
valor_sobrando -= vinte * 20
dez = ((valor_sobrando % 100) % 50) % 20 // 10
valor_sobrando -= dez * 10
cinco = (((valor_sobrando % 100) % 50) % 20) % 10 // 5
valor_sobrando -= cinco * 5
um = ((((valor_sobrando % 100) % 50) % 20) % 10) % 5 // 1

print(f'{valor} -> {cem}x100 {cinquenta}x50 {vinte}x20 {dez}x10 {cinco}x5 {um}x1')