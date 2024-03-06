entrada = input("Por favor ingrese palabras (pueden repetirse) separadas por espacios para formar una lista: ")
lista_original = entrada.split()
lista_procesada = []
for elemento in lista_original:
    if elemento not in lista_procesada:
        lista_procesada.append(elemento)
print("La lista procesada (eliminando elementos repetidos) es: ", lista_procesada)