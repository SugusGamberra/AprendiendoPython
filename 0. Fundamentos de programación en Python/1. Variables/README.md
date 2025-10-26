# VARIABLES

## Introducción

Las variables se usan para guardar datos que el programa necesita durante la ejecución (números, textos, fechas...). Son como cajitas donde guardas información temporal.

## Estructura de la variable

- Nombre: Cómo la identificas (string usuario, int puntuacion...)
- Valor: Lo que guarda la variable

No podemos llamar a la variable de cualquier forma, tienes que tenerlas bien organizadas! Existen unas normas para que su uso no sea un dolor de cabeza ni de errores!

- No pueden empezar por un numero.
- No pueden tener espacios.
- Nada de caracteres raros, salvo _.
- Python distingue mayusculas y minusculas, por lo que edad y Edad serian dos variables diferentes.
- Buena práctica: Empieza siempre en minúsculas, si son varias palabras para separarlas usa mayúsculas: edadUsuario.

## Cómo se declara?

Para declarar (crear) una variable en Python no nos comemos la cabeza. No tienes que decirle que tipo de valor almacena, la estructura es siempre nombreVariable = valor.

Aquí el = no es como en mates, significa "oye mi variable almacena este valor".

Ejemplo de variables en Python:

nombre = "Mario"

edad = 33

precio = 38.99

VIP = false

## Cómo se usa?

Pues una vez la tienes declarada tan solo usa su nombre para ver lo que contiene o trabajar con ella, por ejemplo:

nombre = "Mario"
edad = 33

print(nombre)
print(edad)

## Concatenar

Si queremos unir texto con variables, o juntar varias variables, concatenamos con el simbolo ,. Con el ejemplo anterior haríamos:

print("Me llamo ", nombre, " y tengo ", edad, " años")

También podemos concatenar de la siguiente forma:

palabra1 = "Fundamentos "
palabra2 = "de "
palabra3 = "Programacion"

fraseCompleta = palabra1 + palabra2 + palabra3

print(fraseCompleta)

# COMENTARIOS

Para hacer comentarios en Python usamos el símbolo #. Los comentarios se usan para explicar tu código, bien para ti o si trabajas en equipo, de esta forma mantienes todo explicado y organizado!

Y por hoy ya estaria!!

Así que nada, un print("abrazote ;D") para ti!