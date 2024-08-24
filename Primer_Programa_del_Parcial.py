# Solicitar al usuario un número entero
num = int(input("Introduce un número entero: "))

# Verifica si el número es positivo, negativo o cero
if num > 0:
    # Imprimir todos los números pares desde 1 hasta el número dado
    print("Números pares desde 1 hasta", num, ":")
    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()
elif num < 0:
    # Imprimir todos los números impares desde el número dado hasta 0
    print("Números impares desde", num, "hasta 0:")
    for i in range(num, 1):
        if i % 2 != 0:
            print(i, end=' ')
    print()

else:
    # Lista de nombres de compañeros de clase
    compañeros = ["Armando Say", "Omar Herrera", "Neytan Morales", "Carlos Tzunún", "Melisa Tzic"]
    print("Lista de nombres de mis compañeros de clase:")
    for nombre in compañeros:
        print(nombre)
