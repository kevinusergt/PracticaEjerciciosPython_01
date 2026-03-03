Sueldo_mensual = float(input("Cual es su sueldo mensual? "))

if Sueldo_mensual < 1500000:
    print ("Bueno, no paga impuesto")

elif 1500000 <= Sueldo_mensual <= 3000000:
    Impuesto = Sueldo_mensual * 0.05
    Sueldo_neto = Sueldo_mensual - Impuesto
    
    print("Usted paga", Impuesto)
    print("Su sueldo neto es:", Sueldo_neto)

elif Sueldo_mensual >= 3000000:
    Impuesto1 = Sueldo_mensual * 0.1
    Sueldo_neto1 = Sueldo_mensual - Impuesto1

    print("Usted paga", Impuesto1)
    print("Su sueldo neto es:", Sueldo_neto1)




