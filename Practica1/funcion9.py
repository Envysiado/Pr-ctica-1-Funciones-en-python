#Función que agregue un elemento a una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def agregar_elemento_a_tupla(tupla, elemento):
    nueva_tupla = tupla + (elemento,)
    return nueva_tupla

# Ejemplo de uso:
mi_tupla = (1, 2, 3)
print(mi_tupla)
nuevo_elemento = 4
nueva_tupla = agregar_elemento_a_tupla(mi_tupla, nuevo_elemento)
print(nueva_tupla)  # Imprimirá (1, 2, 3, 4)
