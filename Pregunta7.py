a = float(input("Inserte un número: "))
b = float(input("Inserte otro número: "))
print("A continuación escriba un número del 1 al 3 para escoger entre las siguientes opciones: ")
print("1. Mostrar una suma de los dos números.")
print("2. Mostrar una resta de los dos números (el primero menos el segundo).")
print("3. Mostrar una multiplicación de los dos números")
c = int(input())
if c == 1:
    suma = a+b
    print(f"La suma de los dos números es {suma}")
elif c == 2:
    resta = a-b
    print(f"La resta de los dos números (el primero menos el segundo) es {resta}")
elif c == 3:
    mult = a*b
    print(f"La multiplicación de los dos números es {mult}")
else:
    print("El caracter introducido no es válido.")