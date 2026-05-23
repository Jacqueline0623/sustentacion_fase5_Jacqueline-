sesiones = [
    [101, 250, 10],
    [102, 45, 2],
    [103, 120, 5],
    [104, 300, 12],
    [105, 50, 7]
]

# Función para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"  

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"

# Mostrar informe
print("INFORME DE COMPROMISO\n")

for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente,
          "- Clasificación:", clasificacion)