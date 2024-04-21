#Función que regrese la diferencia de dos conjuntos
def diferencia_de_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto1.difference(conjunto2)
    return diferencia

# Ejemplo de uso:
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
print(conjunto1)
print(conjunto2)
diferencia = diferencia_de_conjuntos(conjunto1, conjunto2)
print(diferencia)  # Imprimirá {1, 2, 3}
