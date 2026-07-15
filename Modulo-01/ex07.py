horas_trabalhas = float(input())
valor_hora = float(input())

excedido = 0.0

if horas_trabalhas > 40:
    excedido = horas_trabalhas - 40
    horas_trabalhas = 40

total = (horas_trabalhas * valor_hora) + (excedido * valor_hora) * 1.5

print(total)