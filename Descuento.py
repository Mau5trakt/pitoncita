edad = int(input("Introduzca su edad: "))
cr = input("digame su tipo de carné (E: Estudiante, P: Pensionista,"
           " F: Familia numerosa, N: No tiene carné): ")
if (25 <= edad <=35 and cr == 'E') or edad <= 10 or (edad >= 65 and cr == 'P') or cr == 'F':
    print("Usted aplica a descuento")
else:
    print("Lo siento pero usted no aplica a descuento para entrar al Zoologico. ")

