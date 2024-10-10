print(" ")
print("Arzaba Diaz April")
def numeros_loteria():
    """
    Pide los numeros triunfadores de la loteria y los muestra en orden de menor a mayor.
    """
    numeros_loteria = []
    
    while True:
        numero = input("Ingresa un numero triunfador de la loteria (o 'fin' para terminar): ")
        if numero.lower() == 'fin':
            break
        else:
            numeros_loteria.append(int(numero))

    numeros_loteria.sort()
    
    print("Numeros triunfadores de la loteria en orden de menor a mayor:")
    print(numeros_loteria)

# Llamar a la funcion
numeros_loteria()
