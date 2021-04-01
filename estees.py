import random
nombre = input("Escriba su nombre: ")
if nombre == 'Marcio':
    print("Mi estimado Mario, su porcentaje de hetero es 0%")
else:
    print("Mi estimado ",nombre,"su porcentaje de hétero es: ", random.randint(0,100),"%")
