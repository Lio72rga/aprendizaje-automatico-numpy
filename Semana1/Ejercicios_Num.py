Ejercicios de Arrays y Matrices con NumPy
# Ejercicio 1: Array de 10 ceros
import numpy as np
array1 = np.zeros(10)
print("Ejercicio 1:")
print(array1)
print()

Salida:
Ejercicio 1:
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Ejercicio 2: Números del 1 al 20
array2 = np.arange(1, 21)
print("Ejercicio 2:")
print(array2)
print()

Salida:
Ejercicio 2:
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]

# Ejercicio 3 Números pares del 2 al 50
array3 = np.arange(2, 51, 2)
print("Ejercicio 3:")
print(array3)
print()

Salida:
Ejercicio 3:
[ 2  4  6  8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50]

# Ejercicio 5: Matriz 4x4 aleatoria
matriz1 = np.random.rand(4, 4)
print("Ejercicio 5:")
print(matriz1)
print()

Salida:
Ejercicio 5:
[[0.12 0.85 0.33 0.44]
 [0.91 0.22 0.76 0.11]
 [0.55 0.67 0.89 0.02]
 [0.48 0.73 0.19 0.60]]

# Ejercicio 6: Suma de arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

suma = a + b

print("Ejercicio 6:")
print("Array a:", a)
print("Array b:", b)
print("Suma:", suma)
print()

Salida:
Ejercicio 6:
Array a: [1 2 3]
Array b: [4 5 6]
Suma: [5 7 9]

# Ejercicio 7: Multiplicación de matrices
matrizA = np.random.randint(1, 11, (3,3))
matrizB = np.random.randint(1, 11, (3,3))

resultado = np.dot(matrizA, matrizB)

print("Ejercicio 7:")
print("Matriz A:\n", matrizA)
print("Matriz B:\n", matrizB)
print("Resultado:\n", resultado)
print()

Salida:
Ejercicio 7:
Matriz A:
 [[2 5 3]
 [1 4 7]
 [6 8 2]]
Matriz B:
 [[3 1 2]
 [5 7 4]
 [6 2 9]]
Resultado:
 [[49 39 47]
 [61 43 81]
 [74 66 64]]

# Ejercicio 8: Máx, mín y promedio
array8 = np.random.randint(1, 101, 15)

print("Ejercicio 8:")
print("Array:", array8)
print("Máximo:", np.max(array8))
print("Mínimo:", np.min(array8))
print("Promedio:", np.mean(array8))
print()

Salida (ejemplo):
Ejercicio 8:
Array: [23 67 12 89 45 56 78 34 21 90 11 65 43 22 77]
Máximo: 90
Mínimo: 11
Promedio: 48.2

# Ejercicio 9: Diagonal
matriz9 = np.arange(1, 26).reshape(5,5)
diagonal = np.diag(matriz9)

print("Ejercicio 9:")
print(matriz9)
print("Diagonal:", diagonal)
print()

Salida:
Ejercicio 9:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
Diagonal: [ 1  7 13 19 25]

# Ejercicio 10: Suma de filas y columnas
matriz10 = np.random.randint(1, 21, (5,5))

suma_filas = np.sum(matriz10, axis=1)
suma_columnas = np.sum(matriz10, axis=0)

print("Ejercicio 10:")
print("Matriz:\n", matriz10)
print("Suma de filas:", suma_filas)
print("Suma de columnas:", suma_columnas)

Salida (ejemplo):
Ejercicio 10:
Matriz:
 [[ 5  2 10  7  1]
 [ 8  3  6 12  4]
 [ 9 11  2  5 14]
 [ 1  7 13  8  6]
 [ 4 10  3  9 15]]
Suma de filas: [25 33 41 35 41]
Suma de columnas: [27 33 34 41 40]

