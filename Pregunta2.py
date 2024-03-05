consumo = float(input("Gracias por su visita. Indique el total de su consumo en el restaurante: "))
porcent = float(input("¿Qué porcentaje del total le gustaría dejar como propina al mesero? (%): "))
prop = consumo * porcent * 0.01
print(f"Muchas gracias, la propina es de: {round(prop, 2)}")
