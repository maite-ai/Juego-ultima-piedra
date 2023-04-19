import random

# Creo una variable donde se almacena la cantidad de piedras con la que se comienza el juego.
stones = random.choice(range(10, 21))

print("\t * ¡BIENVENID@ AL JUEGO DE LA ÚLTIMA PIEDRA! *")

# Ciclo principal (mientras la cantidad de piedras sea mayor a 0)
while stones > 0:
    print(f"\nHay {stones} piedras")

    # Turno del usuario
    gamer_user = int(input("¿Cuántas piedras vas a retirar? (1 a 3)\n"))
    # Condición: Mientras el usuario ingrese valores por fuera de los permitidos, se le pedirá ingresar otro valor.
    while gamer_user < 1 or gamer_user > 3 or gamer_user > stones:
        gamer_user = int(input("Esa no es una opción válida. Intenta de nuevo.\n"))
    stones -= gamer_user
    if gamer_user == 1 and stones == 0:
        print("Lo lamento... ¡PERDISTE! Pero... ¡Felicidades a la máquina! :D")
        print("\n\t * FIN DEL JUEGO *")
        break

    print("----------------------------")
    # Turno de la máquina
    gamer_machine = random.randint(1, min(3, stones))
    print(f"La máquina retiró {gamer_machine} piedras")
    stones -= gamer_machine
    if stones == 0:
        print("¡GANASTE! ¡Felicidades!")
        print("\n\t * FIN DEL JUEGO *")
        break
