def calcular_multa(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa por retraso según el tipo de usuario.
    """
    if dias_retraso <= 0:
        return 0.0
        
    tipo_usuario = tipo_usuario.lower()
    
    if tipo_usuario == 'alumno':
        tarifa_diaria = 5.0
    elif tipo_usuario == 'profesor':
        tarifa_diaria = 2.0
    elif tipo_usuario == 'administrador':
        tarifa_diaria = 0.0
    else:
        tarifa_diaria = 0.0
        
    multa_total = dias_retraso * tarifa_diaria
    
    if dias_retraso > 30 and multa_total > 0:
        multa_total += multa_total * 0.20
        
    return float(multa_total)

def calcular_multa_match(dias_retraso: int, tipo_usuario: str) -> float:
    """
    Calcula la multa usando match/case.
    """
    if dias_retraso <= 0:
        return 0.0
        
    match tipo_usuario.lower():
        case 'alumno':
            tarifa_diaria = 5.0
        case 'profesor':
            tarifa_diaria = 2.0
        case 'administrador':
            tarifa_diaria = 0.0
        case _:
            tarifa_diaria = 0.0
            
    multa_total = dias_retraso * tarifa_diaria
    
    if dias_retraso > 30 and multa_total > 0:
        multa_total += multa_total * 0.20
        
    return float(multa_total)

def ejecutar_pruebas() -> None:
    """Ejecuta pruebas básicas para calcular_multa."""
    assert calcular_multa(0, "alumno") == 0.0
    assert calcular_multa(5, "alumno") == 25.0
    assert calcular_multa(10, "profesor") == 20.0
    assert calcular_multa(15, "administrador") == 0.0
    assert calcular_multa(40, "alumno") == 240.0
    assert calcular_multa(-5, "profesor") == 0.0
    assert calcular_multa(10, "invitado") == 0.0

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()