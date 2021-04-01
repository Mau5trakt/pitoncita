# Convertir divisas
print('Programa para convertir divisas. Ingrese la opción para realizar la conversión que necesite \n'
      '#1 para convertir de dolares a córdoabas \n'
      '#2 para convertir de córdobas a dólares  \n')
usdnio = 35.10
niousd = 0.028
opcion = int(input("Ingrese una opción:\n"))

if opcion == 1:
    cantidad =int(input("Ingrese la cantidad en Dolares: "))
    dolares = cantidad * usdnio
    print("{} Dólares  son {} Córdobas \n(tasa de cambio a 35.10 Córdobas por Dólar) ".format(cantidad, dolares))
if opcion == 2:
    cantidad = int(input("Ingrese la cantidad en Córdobas: "))
    cordobas = cantidad * niousd
    print("{} Córdobas son ´{} Dólares \n(tasa de cambio a 0.028 Dólares por Córdobas".format(cantidad, cordobas))
else:
    print("Ingrese una opción válida ")






