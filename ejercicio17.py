
kilometros = float(input("Kilometros recorridos: "))
minutos = int(input("Cuantos minutos: "))
if minutos < 10:
    valor = 5000
    print("Valor a pagar:", valor)
else:
    valor = 0
    valor = 800 * kilometros
    print("Valor a pagar:", valor)