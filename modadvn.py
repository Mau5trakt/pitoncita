""" Programa en el que el usuario debe adivinar el número generado por la computadora"""
import random
rndnum = random.randint(1, 10)
name = input("Dime tu nombre: ")
print("Hola,{} en este programa tendras que adivinar el número "
      "que ha generado la máquina entre 1 y 10 Tienes solamente 3 vidas,".format(name))

maxVida = 3  # Numero maximo de vida
while maxVida != 0:
    n = int(input("introduzca un número: "))
    if n == rndnum:
        print("Felicidades, has ganado un Jeno")
    else:
        maxVida = maxVida - 1
        print("No has adivinado, a Jeno le quedan {} vidas".format(maxVida))
if maxVida == 0:
        print("Jeno fue al descanso eterno. Por ciero, el número era {} :P".format(rndnum))
