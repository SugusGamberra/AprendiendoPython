# OPERADORES ARITMETICOS

Estos son los simbolitos que le dicen a Python que operacion aritmetica debe realizar con los valores (ya sean literales o almacenados en variables).

## Operadores básicos

- Suma: +
- Resta: - 
- Multiplicación: *
- División: /
- División entera (quita los decimales): //
- Módulo o resto: % (devuelve el resto de una división)
- Exponenciación (potencias): **

## Que pasa con la concatenación y el simbolo "+"?

Usamos el simbolo + para concatenar textos:

palabra1 = "Hola "
palabra2 = "caraqlo"

fraseCompleta = palabra1 + palabra2

print(fraseCompleta)

Qué ocurre si dices de sumar texto y numero?? Pos se te vuelve loco, te va a dar error xd 

nombre = "Maria"
edad = 67

print("Hola " + nombre + ", tienes " + edad + " años!")

Si queremos que nos lea la edad le tenemos que poner antes str(edad):

print("Hola " + nombre + ", tienes " + str(edad) + " años!")

Aaaaunque también se puede hacer de la siguiente forma:

mensaje = f"Hola {nombre}, tienes {edad} años!"
print(mensaje)

Para hacer operaciones es tan fácil como:

resultado = 10 + 4
print(resultado)

## Asignación aritmética (abreviaturas)

- += : a = a + b 
- -= : a = a - b
- *= : a = a * b
- /= : a = a / b
- %= : a = a % b
- **= : a = a ** b
- //= : a = a // b

## Incremento y decremento

Si vienes de otros lenguajes... no, aquí no hay deso HAHAHAH aquí se hacen con asignaciones aritméticas ya que son mas claras y no añade sintaxis extra xd

## Prioridad de operadores

El orden importa más que el tamaño ñ.ñ

Per sé Python hace primero multiplicaciones, divisiones y el resto, luego hace sumas y restas. Si quieres priorizar un orden concreto debes usar paréntesis, lo que esté dentro se calculará primero!

- Normal: 10 + 5 * 2 = 20 (Primero hace 5*2 y despues suma el resultado con 10)
- Con paréntesis: (10 + 5) * 2 = 30 (Primero hace 10+5 y luego multiplica el resultado por 2)

Ya estaría todo! En un futuro haré una carpeta con ejercicios para que practiques lo que se va viendo ;3

Mientras échale un vistazo al [código](operadoresAritmeticos.py) para que puedas ir viendo lo que explico y lo puedas probar por tu cuenta!