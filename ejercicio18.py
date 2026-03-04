
ancho = int(input("Ancho del cuarto: "))
largo = int(input("Largo del cuarto: "))
area = ancho * largo
print("El area es:", area)

if area < 12:
    print("Es pequeño")
elif 12 <= area <= 20:
    print("Es mediano")

else:
    print("Es grande")