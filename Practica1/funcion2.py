#Función que reciba un diccionario y elimine una clave-valor, retornar el diccionario modificado
def eliminar_valor(diccionario, clave):
    if clave in diccionario:
        del diccionario[clave]
    return diccionario

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(mi_diccionario)
clave_a_eliminar = 'b'
nuevo_diccionario = eliminar_valor(mi_diccionario, clave_a_eliminar)
print(nuevo_diccionario)  # Imprimirá {'a': 1, 'c': 3}


