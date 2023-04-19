import random

# Creo una variable donde se almacena la cantidad de piedras con la que se comienza el juego y una variable auxiliar.
stone_number = random.choice(range(10, 21))
aux = 1

print(f"El juego inicia con {stone_number} piedras")


# Mientras la cantidad sea mayor que la variable aux, pedirle al usuario que ingrese un número entre 1 y 3.
while stone_number >= aux:
    print("\n¡Tu turno!")
    print("----------")
    gamer_u = int(input("Ingresa un número entre 1 y 3: "))

    # Condición: si ingresa uno de los 3 valores, se descuenta ese valor de la cantidad.
    if gamer_u > 3:
        print("¡No permitido! Tienes que tomar 1, 2 ó 3 piedras\n")
        stone_number = stone_number
    else:
        print(f"Retiraste {gamer_u} piedras")
        stone_number -= gamer_u
        print(f"Quedan {stone_number} piedras")
        if stone_number == 0:
            print("¡PERDISTE!")

        # Ahora le toca jugar a la máquina
        print("\nEs el turno de la máquina")
        print("----------------------------")
        if stone_number > 3:
            machine = random.choice(range(1, 4))
            print(f"La máquina retira {machine} piedras")
            stone_number -= machine
        elif stone_number == 2:
            print("La máquina retira 1 piedra")
            stone_number -= 1
        else:
            stone_number -= 1
            print("¡GANASTE! Fin del juego")

    print(f"Quedan {stone_number} piedras")
