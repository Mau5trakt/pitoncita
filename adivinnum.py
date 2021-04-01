import random
rndnum = random.randint(1, 10)
name = input("Dime tu nombre: ")
print("Hola,{} en este programa tendras que adivinar el número "
      "que ha generado la máquina entre 1 y 10 Tienes solamente 3 vidas".format(name))
print(rndnum)
maxVida = 3  # Numero maximo de vida

while maxVida != 0:
    n = int(input("introduzca un número: "))
    if (n<11 and n>0):
        if n == rndnum:
            print("Felicidades, has acertado")
            break
        else:
            maxVida = maxVida - 1
            print("No has adivinado, te quedan {} vidas".format(maxVida))
    else:
        print("Ingrese un numero correcto")
    if maxVida == 0:
            print("el número era {} :P".format(rndnum))