''' Pide al usuario que introduzca 5 números e imprime
el numero menor y el número mayor '''
nombre = input("Introduzca su nombre: ")
print("hola, ", nombre  ,"ingrese 5 números y luego se le imprimira el número mayor y el número menor")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
c = int(input("Ingrese un número: "))
d = int(input("Ingrese un número: "))
e = int(input("Ingrese un número: "))

print("El numero mayor entre {} {} {} {} {} es: {} "
      .format(a,b,c,d,e, max(a,b,c,d,e)))
print("El numero menor entre {} {} {} {} {} es: {} "
      .format(a,b,c,d,e, min(a,b,c,d,e)))