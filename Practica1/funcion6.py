#Función que elimine un elemento de un conjunto, retornar verdadero si pudo eliminar y falso si no pudo

def eliminar_elemento(conjunto, elemento):
    if elemento in conjunto:
        conjunto.remove(elemento)
        return True
    else:
        return False

# Ejemplo de uso:
mi_conjunto = {1, 2, 3, 4}
print(mi_conjunto)
elemento_a_eliminar = 3
resultado = eliminar_elemento(mi_conjunto, elemento_a_eliminar)
print(resultado)  # Imprimirá True (porque el elemento 3 se elimina exitosamente)
print(mi_conjunto)  # Imprimirá {1, 2, 4}

print("_______________________________________________________")
# Intentaremos eliminar un elemento que no está en el conjunto
mi_conjunto = {1, 2, 3, 4}
print(mi_conjunto)
elemento_a_eliminar = 5
resultado = eliminar_elemento(mi_conjunto, elemento_a_eliminar)
print(resultado)  # Imprimirá False (porque el elemento 5 no está en el conjunto)
print(mi_conjunto)
