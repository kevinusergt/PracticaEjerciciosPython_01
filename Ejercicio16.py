

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 60:
    print("Aprobado")

elif promedio >= 55:
    print("Vas a habilitación")

else:
    print("Reprobaste")