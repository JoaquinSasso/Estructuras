def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso:
print(factorial_iterativo(10000))  # Output: 120
