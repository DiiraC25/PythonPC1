time = input("Por favor, ingrese la hora actual en formato HH:MM. ")
h, m = time.split(":")
if 7 <= int(h) <= 8 and 0 <= int(m) <= 60:
    print("Es la hora del desayuno")
elif 12 <= int(h) <= 13 and 0 <= int(m) <= 60:
    print("Es la hora del almuerzo")
elif 6 <= int(h) <= 19 and 0 <= int(m) <= 60:
    print("Es la hora de la cena")