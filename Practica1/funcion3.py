#Función que reciba un diccionario y modifique el valor de una clave, retornar verdadero si pudo modificar y falso si no pudo

def modificar_valor(diccionario, clave, nuevo_valor):
    if clave in diccionario:
        diccionario[clave] = nuevo_valor
        return True
    else:
        return False

# Ejemplo de uso True:
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
print(diccionario1)
clave_a_modificar = 'b'
nuevo_valor = 10
resultado = modificar_valor(diccionario1, clave_a_modificar, nuevo_valor)
print(resultado)  # Imprimirá True
print(diccionario1)  # Imprimirá {'a': 1, 'b': 10, 'c': 3}

print("_________________________________")

# Ejemplo de uso False:
diccionario2 = {'a': 1, 'b': 2, 'c': 3}
print(diccionario2)
clave_a_modificar = 'd'  # Clave que no existe en el diccionario
nuevo_valor = 10
resultado = modificar_valor(diccionario2, clave_a_modificar, nuevo_valor)
print(resultado)  # Imprimirá False
print(diccionario2)  