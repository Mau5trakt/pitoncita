import random

nombre = input("introduzca su nombre: ")
pr_hetero = random.randint(0, 100)  # <-- Variable que almacena el %
if 'marcio' == nombre.lower():
    print("Su porcentaje de hetero es 0%")
else:
    print(f"Mi estimado {nombre} su porcentaje de hetero es: {pr_hetero}")
