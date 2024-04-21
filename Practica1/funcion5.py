#Función que agregue elementos a un conjunto, retornar verdadero si pudo agregar y falso si no pudo.
def agregar_elementos(conjunto, *elementos):
    elementos_agregados = False
    for elemento in elementos:
        if elemento not in conjunto:
            conjunto.add(elemento)
            elementos_agregados = True
    return elementos_agregados

# Ejemplo de uso:
mi_conjunto = {1, 2, 3}
print(mi_conjunto)
elemento1 = 3  # Este elemento ya existe en el conjunto
elemento2 = 4
resultado = agregar_elementos(mi_conjunto, elemento1, elemento2)
print(resultado)  # Imprimirá True (porque al menos un elemento nuevo se agregó)
print(mi_conjunto)  # Imprimirá {1, 2, 3, 4}

print("____________________________________________")
mi_conjunto = {1, 2, 3}
print(mi_conjunto)
# Intentaremos agregar elementos que ya están en el conjunto
resultado = agregar_elementos(mi_conjunto, 2, 3)
print(resultado)  # Imprimirá False (no se agregaron elementos nuevos)
print(mi_conjunto)  # El conjunto sigue siendo {1, 2, 3, 4}
