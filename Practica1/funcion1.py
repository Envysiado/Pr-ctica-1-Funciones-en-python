#Función que reciba un diccionario y agregar una clave-valor, retornar el diccionario modificado (Debe agregarlo al final)

def agregarValor(diccionario, clave, valor):
    diccionario[clave] = valor
    return diccionario

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2}
print(mi_diccionario)
mi_diccionario_modificado = agregarValor(mi_diccionario, 'c', 3)
print(mi_diccionario_modificado)  

# Salida: {'a': 1, 'b': 2, 'c': 3}
