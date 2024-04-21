# Prctica 1 Funciones en python

# Reporte de Funciones en Python

A continuación se presentan una serie de funciones en Python junto con su descripción y ejemplos de uso:

1. **Función agregarValor(diccionario, clave, valor):**
   - Descripción: Esta función recibe un diccionario y agrega una nueva clave-valor al final del mismo. Luego, retorna el diccionario modificado.
   - Ejemplo de uso:
     ```python
    mi_diccionario = {'a': 1, 'b': 2}
    mi_diccionario_modificado = agregarValor(mi_diccionario, 'c', 3)
    print(mi_diccionario_modificado)  # Salida: {'a': 1, 'b': 2, 'c': 3}
    ```

2. **Función eliminar_valor(diccionario, clave):**
   - Descripción: Esta función recibe un diccionario y una clave, y elimina la clave-valor correspondiente del diccionario. Retorna el diccionario modificado.
   - Ejemplo de uso:
     ```python
    mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
    clave_a_eliminar = 'b'
    nuevo_diccionario = eliminar_valor(mi_diccionario, clave_a_eliminar)
    print(nuevo_diccionario)  # Imprimirá {'a': 1, 'c': 3}
    ```

3. **Función modificar_valor(diccionario, clave, nuevo_valor):**
   - Descripción: Esta función recibe un diccionario, una clave y un nuevo valor. Modifica el valor asociado a la clave dada en el diccionario. Retorna True si pudo modificar el valor y False si no pudo (porque la clave no existe en el diccionario).
   - Ejemplo de uso True:
     ```python
    diccionario1 = {'a': 1, 'b': 2, 'c': 3}
    clave_a_modificar = 'b'
    nuevo_valor = 10
    resultado = modificar_valor(diccionario1, clave_a_modificar, nuevo_valor)
    print(resultado)  # Imprimirá True
    print(diccionario1)  # Imprimirá {'a': 1, 'b': 10, 'c': 3}
    ```
   - Ejemplo de uso False:
     ```python
    diccionario2 = {'a': 1, 'b': 2, 'c': 3}
    clave_a_modificar = 'd'  # Clave que no existe en el diccionario
    nuevo_valor = 10
    resultado = modificar_valor(diccionario2, clave_a_modificar, nuevo_valor)
    print(resultado)  # Imprimirá False
    print(diccionario2)  # Imprimirá {'a': 1, 'b': 2, 'c': 3} (el diccionario no se ha modificado)
    ```

4. **Función combinar_diccionarios(dic1, dic2):**
   - Descripción: Esta función combina dos diccionarios y retorna el diccionario resultante.
   - Ejemplo de uso:
     ```python
    diccionario1 = {'a': 1, 'b': 2}
    diccionario2 = {'c': 3, 'd': 4}
    diccionario_combinado = combinar_diccionarios(diccionario1, diccionario2)
    print(diccionario_combinado)  # Imprimirá {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ```

5. **Función agregar_elementos(conjunto, *elementos):**
   - Descripción: Esta función agrega elementos a un conjunto y retorna True si pudo agregar al menos un elemento nuevo, y False si no pudo agregar ninguno.
   - Ejemplo de uso:
     ```python
    mi_conjunto = {1, 2, 3}
    elemento1 = 3  # Este elemento ya existe en el conjunto
    elemento2 = 4
    resultado = agregar_elementos(mi_conjunto, elemento1, elemento2)
    print(resultado)  # Imprimirá True (porque al menos un elemento nuevo se agregó)
    print(mi_conjunto)  # Imprimirá {1, 2, 3, 4}
    ```

6. **Función eliminar_elemento(conjunto, elemento):**
   - Descripción: Esta función elimina un elemento de un conjunto y retorna True si el elemento se elimina exitosamente, y False si el elemento no está presente en el conjunto.
   - Ejemplo de uso:
     ```python
    mi_conjunto = {1, 2, 3, 4}
    elemento_a_eliminar = 3
    resultado = eliminar_elemento(mi_conjunto, elemento_a_eliminar)
    print(resultado)  # Imprimirá True (porque el elemento 3 se elimina exitosamente)
    print(mi_conjunto)  # Imprimirá {1, 2, 4}
    ```

7. **Función combinar_conjuntos(conjunto1, conjunto2):**
   - Descripción: Esta función combina dos conjuntos y retorna el conjunto resultante.
   - Ejemplo de uso:
     ```python
    conjunto1 = {1, 2, 3}
    conjunto2 = {4, 5, 6}
    conjunto_combinado = combinar_conjuntos(conjunto1, conjunto2)
    print(conjunto_combinado)  # Imprimirá {1, 2, 3, 4, 5, 6}
    ```

8. **Función diferencia_de_conjuntos(conjunto1, conjunto2):**
   - Descripción: Esta función retorna la diferencia de dos conjuntos (elementos presentes en conjunto1 pero no en conjunto2).
   - Ejemplo de uso:
     ```python
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {4, 5, 6, 7, 8}
    diferencia = diferencia_de_conjuntos(conjunto1, conjunto2)
    print(diferencia)  # Imprimirá {1, 2, 3}
    ```

9. **Función agregar_elemento_a_tupla(tupla, elemento):**
   - Descripción: Esta función agrega un elemento a una tupla y retorna la nueva tupla resultante.
   - Ejemplo de uso:
     ```python
    mi_tupla = (1, 2, 3)
    nuevo_elemento = 4
    nueva_tupla = agregar_elemento_a_tupla(mi_tupla, nuevo_elemento)
    print(nueva_tupla)  # Imprimirá (1, 2, 3, 4)
    ```

10. **Función concatenar_tuplas(tupla1, tupla2):**
    - Descripción: Esta función concatena dos tuplas y retorna la nueva tupla resultante.
    - Ejemplo de uso:
      ```python
     tupla1 = (1, 2, 3)
     tupla2 = ('a', 'b', 'c')
     nueva_tupla = concatenar_tuplas(tupla1, tupla2)
     print(nueva_tupla)  # Imprimirá (1, 2, 3, 'a', 'b', 'c')
     ```

11. **Función revertir_tupla(tupla):**
    - Descripción: Esta función revierte el orden de una tupla y retorna la nueva tupla resultante.
    - Ejemplo de uso:
      ```python
     mi_tupla = (1, 2, 3, 4, 5)
     tupla_revertida = revertir_tupla(mi_tupla)
     print(tupla_revertida)  # Imprimirá (5, 4, 3, 2, 1)
     ```

12. **Función imprimir_diccionario(diccionario):**
    - Descripción: Esta función recibe un diccionario y lo imprime.
    - Ejemplo de uso:
      ```python
     mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
     imprimir_diccionario(mi_diccionario)
     ```

13. **Función imprimir_conjunto(conjunto):**
    - Descripción: Esta función recibe un conjunto y lo imprime.
    - Ejemplo de uso:
      ```python
     mi_conjunto = {1, 2, 3, 4, 5}
     imprimir_conjunto(mi_conjunto)
     ```

---
