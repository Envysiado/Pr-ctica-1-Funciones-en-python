#Función que combine dos conjuntos, regresar el conjunto resultante

def combinar_conjuntos(conjunto1, conjunto2):
    conjunto_resultante = conjunto1.union(conjunto2)
    return conjunto_resultante

# Ejemplo de uso:
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5 ,6}
print(conjunto1)
print(conjunto2)
conjunto_combinado = combinar_conjuntos(conjunto1, conjunto2)
print(conjunto_combinado)  # Imprimirá {1, 2, 3, 4, 5}
