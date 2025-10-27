# Operadores aritméticos

# Concatenar

palabra1 = "Hola "
palabra2 = "caracola"

print(palabra1 + palabra2)

palabraCompleta = palabra1 + palabra2

print(palabraCompleta)

# Sumar texto + numero

nombre = "Maria"
edad = 67

# Esto te daría error, puedes hacer la prueba borrando el "#" del principio!

# print("Hola " + nombre + ", tienes " + edad + " años!")

# Para que te lo imprima tienes que pasar la variable edad (tipo int) a texto (tipo string) de la siguiente forma:

print("Hola " + nombre + ", tienes " + str(edad) + " años!")

# Otra forma de hacerlo muy chula es:

mensaje = f"Hola {nombre}, tienes {edad} años!"

print(mensaje)

# Para hacer operaciones es tan fácil como:

resultado = 10 + 4

print(resultado)

# Asignación aritmética

puntuacion = 100
print(puntuacion)

puntuacion += 10
print(puntuacion)

puntuacion -= 5
print(puntuacion)

puntuacion *= 2
print(puntuacion)

puntuacion /= 2
print(puntuacion)

puntuacion %= 2
print(puntuacion)

puntuacion **= 2
print(puntuacion)

puntuacion //= 2
print(puntuacion)

# Prioridad de operadores

operacion1 = 10 + 5 * 2
operacion2 = (10 + 5) * 2
print(operacion1)
print(operacion2)