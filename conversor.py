def conversor (tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")


menu = """
Bienvenido perrito 🐶


1 - Lempiras
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion =int(input(menu))

if opcion == 1:
    conversor("hondureños", 24.5)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
   conversor("mexicanos", 25)
else:
    print('ingresa una opcion correcta por favor')
