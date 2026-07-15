segundos = int(input())

horas = int(segundos / 60 ** 2)
minutos = int((segundos % 60 ** 2) / 60)
segundos_restantes = segundos % 60 

print(f"{horas}:{minutos}:{segundos_restantes}")