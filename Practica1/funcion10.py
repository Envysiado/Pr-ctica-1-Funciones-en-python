#Función que concatene dos tuplas en una nueva, regresar la nueva tupla
def concatenar_tuplas(tupla1, tupla2):
    nueva_tupla = tupla1 + tupla2
    return nueva_tupla

# Ejemplo de uso:
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
print(tupla1)
print(tupla2)
nueva_tupla = concatenar_tuplas(tupla1, tupla2)
print(nueva_tupla)  # Imprimirá (1, 2, 3, 'a', 'b', 'c')
