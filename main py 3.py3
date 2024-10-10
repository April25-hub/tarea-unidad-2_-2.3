print(" ")
print("Arzab Diaz April 3W 1173")
def es_email_valido(email):
    """
    verifica si la dirección de email es válida.
    
    Un email es considerado válido si contiene el símbolo '@'.
    
    args:
        email (str): La dirección de email a validar.
        
    returns:
        bool: True si el email es válido, False en caso contrario.
    """
    return '@' in email

#esta linea capturara la dirección de email del usuario
email_usuario = input("por favor, introduce tu dirección de email: ")

#estab linea verificara la validez del email
if es_email_valido(email_usuario):
    print("la dirección de email es válida.")
else:
    print("la dirección de email no es válida.")
