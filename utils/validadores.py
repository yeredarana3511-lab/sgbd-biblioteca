"""
Valida si un ISBN-13 es correcto.
"""
def validar_isbn13(isbn: str) -> bool:
    if len(isbn) != 13:
        return False
        
    if not isbn.isdigit():
        return False
        
    suma_total = 0
    
    for indice in range(13):
        digito = int(isbn[indice])
        
        if indice % 2 == 0:
            suma_total += digito * 1
        else:
            suma_total += digito * 3
            
    return suma_total % 10 == 0

"""
Valida si un email tiene formato básico correcto.
"""
def validar_email(email: str) -> bool:
    if email.count('@') != 1:
        return False
        
    usuario, dominio = email.split('@')
    
    if len(usuario) == 0:
        return False
        
    if len(dominio) == 0:
        return False
        
    if '.' not in dominio:
        return False
        
    if dominio.startswith('.') or dominio.endswith('.'):
        return False
        
    return True