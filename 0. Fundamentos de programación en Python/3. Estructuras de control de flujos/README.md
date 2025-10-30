# ESTRUCTURAS DE CONTROL DE FLUJOS

De momento estamos ejecutando código línea por línea. Estas estructuras nos sirven para saltar lineas, repetir bloques o ejecutar código con condicionales!

### Operadores de comparación

- Igual que: ==
- Distinto que: !=
- Mayor que: >
- Mayor o igual que: >=
- Menor que: <
- Menor o igual que: <=

### Operadores lógicos

- Y: and
    - if edad >= 18 and esEstudiante_daw: // es verdadero (true) si ambos son true
- O: or
    - if edad > 65 or esEstudiante_daw: // Al menos una debe ser true
- No: not
    - if not tieneEntrada: // Si tieneEntrada es true, not tieneEntrada seria false

## Condicionales

### If/Else

En Python tenemos que tener en cuenta que la linea del if SIEMPRE termina con ":", esto le dice a Python "oye aqui empieza el bloque de lo que debes hacer si esta condicion se cumple". La indetación dentro del if es super importante, asi que atinale al tab cuando le metas tus condiciones al if!!!

edad = 20

if edad >= 18:
    print ("Eres mayor de edad!!")
else:
    print ("tas chikito uwu no puedes pasar!!!")
    
### ELif (vamos el else if pero python es muy cool jiji)

nota = 7

if nota == 10:
    print("boh, fieroteeee!!")
elif nota >= 6:
    print("not bad")
elif nota == 5:
    print("por los pelosssss")
else:
    print("palmaste colega :c")

## Bucles

Nos permiten recorrer un trozo de código varias veces sin tener que escribirlo 40 veces. Python no tiene ni do...while ni switch! Por que? Porque con un while true y un break tienes un do while, y con el switch pues... tenemos un analogo! Ahora lo vemos ;D

Cuidado con los bucles infinitos!! SIEMPRE rompe el bucle o metele algo dentro que haga que la condicion termine en algun punto!!

- Break: Rompe el bucle por completo y se sale, sin importar nada más!
- Continue: No rompe el bucle, pero se salta todo lo que queda de la iteracion y pasa directamente a la siguiente.

### While

Mientras x condición se cumple, haz tal cosa. 

contador = 1

while contador <= 5:
    print(f"El contador vale: {contador}")
    contador += 1

print("El bucle while ha terminado!")

### For

En Python, for no es un contador, está diseñado para recorrer colecciones (listas, textos, etc) uno por uno. Para cada elemento que haya en esta coleccion, haz tal cosa.

lstInvitados = ["Sahoro", "Gemma", "Anastasio", "Alisa Melano"]

for nombre in lstInvitados:
    print(f"Bienvenide mi estimade {nombre}")

print("Lista finalizada")

#### Range

Para repetir un numero determinado de veces algo usamos range!

for numero in range(5):
    print(f"Repeticion del numero {numero}")

### Structural Pattern Matching (match...case)

El análogo del switch pero mejoradisimo!!!

comando = "atacar"

match comando:
    case "atacar":
        print("Has lanzado un ataque")
    case "defender":
        print("Te has defendido!")
    case "usarItem":
        print("Abres la mochila...")
    case _: # Esto es el default o el else digamos
        print("No se reconoce este comando")

Puedes ojear el [código](./controlFlujo.py), bajarlo, probarlo... yatusae ;D