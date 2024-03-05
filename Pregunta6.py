edad = int(input("Por favor, ingrese su edad: "))
if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
else:
    precio = 10
print(f"El precio de su entrada es de ${precio}")