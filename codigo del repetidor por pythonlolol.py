import os
veces = int(input("escriba las veces "))
programa = input("escriba start y el nombre del programa ")
repeticiones = 0
while True:
    os.system(programa)
    repeticiones += 1
    print(repeticiones)
    if repeticiones == veces:
        break