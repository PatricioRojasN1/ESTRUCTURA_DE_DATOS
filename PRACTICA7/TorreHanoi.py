def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return

    # Mover n-1 discos al auxiliar
    hanoi(n-1, origen, destino, auxiliar)

    # Mover el disco más grande
    print(f"Mover disco {n} de {origen} a {destino}")

    # Mover n-1 discos al destino
    hanoi(n-1, auxiliar, origen, destino)

hanoi(2, "A", "B", "C")