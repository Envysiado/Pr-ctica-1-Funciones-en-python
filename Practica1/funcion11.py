#Función que revertir el orden de una tupla y lo guarde los cambios en una tupla nueva, regresar la nueva tupla
def revertir_tupla(tupla):
    nueva_tupla = tupla[::-1]
    return nueva_tupla

# Ejemplo de uso:
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
tupla_revertida = revertir_tupla(mi_tupla)
print(tupla_revertida)  # Imprimirá (5, 4, 3, 2, 1)
