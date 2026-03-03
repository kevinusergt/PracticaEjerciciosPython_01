Precio_producto = float(input("Que valor tiene su producto? "))
Descuento = Precio_producto * 0.1
precio_final = Precio_producto - Descuento

if Precio_producto > 100000:
    print(f"El precio final para este producto es {precio_final}")
else:
    print("El precio del producto es:", Precio_producto)    