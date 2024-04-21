#Función que combine dos diccionarios, regresar el diccionario resultante
def combinar_diccionarios(dic1, dic2):
    dic_resultante = dic1.copy()  # Copiamos el primer diccionario para no modificarlo directamente
    dic_resultante.update(dic2)    # Actualizamos el primer diccionario con los elementos del segundo
    return dic_resultante

# Ejemplo de uso:
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'c': 3, 'd': 4}
print(diccionario1)
print(diccionario2)
diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
print(diccionario_combinado)  # Imprimirá {'a': 1, 'b': 2, 'c': 3, 'd': 4}
