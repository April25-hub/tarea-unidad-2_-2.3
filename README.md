# tarea-unidad-2_-2.3

Arzaba Diaz April 1174 3W

print(" ")

print("Arzaba Diaz April 3W 1173")

def factorial(n):

    """
    
    calcula el factorial de un numero entero positivo n.

    
    
    args:
    
    n (int): Un entero positivo del cual se desea calcular el factorial.

    
    
    returns:
    
    int: el factorial de n.
    
    """
    
    if n < 0:
    
        raise ValueError("El numero debe ser positivo.")

    
    
    resultado = 1
    
    for i in range(1, n + 1):
    
        resultado *= i

    
    
    return resultado


#esta linea me dara un ejemplo de uso

numero = 5

resultado_factorial = factorial(numero)

print(f"El factorial de {numero} es {resultado_factorial}.")
![image](https://github.com/user-attachments/assets/07b145a5-24fa-4caf-904e-5df4a01fe415)
![image](https://github.com/user-attachments/assets/7008ed55-8d44-4248-9703-677d45055312)



