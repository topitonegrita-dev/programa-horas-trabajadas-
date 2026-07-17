#---------------------------------------------
# Problema 5
# Oscar fernando Monsalve 
# Fundamentos de programacion 
# autor programa 
# Control de horas trabajadas por recursos
#---------------------------------------------

HORAS_ESTANDAR = 40


recursos = [
    ["Juan", 8, 8, 8, 8, 8],
    ["María", 9, 9, 8, 9, 8],
    ["Carlos", 7, 8, 7, 8, 7],
    ["Ana", 10, 9, 9, 8, 9]
]



def calcular_horas(fila):
    """
    Calcula el total de horas semanales y
    clasifica la jornada laboral.
    """
    total = sum(fila[1:])

    if total > HORAS_ESTANDAR:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion



print("=" * 55)
print("CONTROL DE HORAS TRABAJADAS")
print("=" * 55)

for recurso in recursos:

    nombre = recurso[0]

    total, clasificacion = calcular_horas(recurso)

    print(f"\nRecurso: {nombre}")
    print(f"Total de horas: {total}")
    print(f"Clasificación: {clasificacion}")
