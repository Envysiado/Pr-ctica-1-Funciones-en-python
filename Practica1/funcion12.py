#Función que recibe un diccionario y lo imprime
def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f'{clave}: {valor}')

# Ejemplo de uso:
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
imprimir_diccionario(mi_diccionario)
