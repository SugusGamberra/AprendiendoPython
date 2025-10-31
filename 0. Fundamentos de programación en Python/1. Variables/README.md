# 🧠 VARIABLES EN PYTHON

## 💬 Introducción

Las variables se usan para guardar datos que el programa necesita durante la ejecución (números, textos, fechas...). Son como cajitas donde guardas información temporal 🗃️

---

## 🧩 Estructura de la variable

- **Nombre**: Cómo la identificas (`usuario`, `puntuacion`...)
- **Valor**: Lo que guarda la variable (`Lucia`, `187`...)

### 📝 Reglas para nombrarlas

#### 🚫 No pueden:

- Empezar por un número
- Tener espacios
- Usar símbolos raros (solo `_` permitido)

⚠️ Python distingue mayúsculas de minúsculas:
`edad` y `Edad` no son lo mismo.

> 💡 Buena práctica: usa minúsculas, y si son varias palabras, separa con mayúsculas:

```python 
edadUsuario = 33
```

---

## ⚙️ Cómo se declara?

Para declarar (crear) una variable en Python no nos comemos la cabeza. No tienes que decirle que tipo de valor almacena, la estructura es siempre `nombreVariable = valor`.

Aquí el `=` no es como en mates, significa "**oye mi variable almacena este valor**".

Ejemplo de variables en Python:

```python
nombre = "Mario"

edad = 33

precio = 38.99

VIP = false
```

---

## 🔍 Cómo se usa?

Pues una vez la tienes declarada tan solo usa su nombre para ver lo que contiene o trabajar con ella, por ejemplo:

```python
nombre = "Mario"
edad = 33

print(nombre)
print(edad)
```

---

## 🔗 Concatenar

Si queremos unir texto con variables, o juntar varias variables, concatenamos con el simbolo `,` o `+`. Con el ejemplo anterior haríamos:

```python
print("Me llamo ", nombre, " y tengo ", edad, " años")
```

También podemos concatenar de la siguiente forma:

```python
palabra1 = "Fundamentos "
palabra2 = "de "
palabra3 = "Programacion"

fraseCompleta = palabra1 + palabra2 + palabra3

print(fraseCompleta)
```

---

# 💬 COMENTARIOS

Para hacer comentarios en Python usamos el símbolo `#`. Los comentarios se usan para explicar tu código, bien para ti o si trabajas en equipo, de esta forma mantienes todo explicado y organizado!

```python
# Esto sería el ejemplo de un comentario en python :3
```

---

> 🎉 Y por hoy ya estaria!!
> Así que nada, un print("abrazote ;D") para ti!