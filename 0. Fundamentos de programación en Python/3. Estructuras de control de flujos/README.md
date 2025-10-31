# 🔁 ESTRUCTURAS DE CONTROL DE FLUJOS

De momento estamos ejecutando código **línea por línea**. Pero a veces queremos saltar lineas, repetir bloques o ejecutar código con condicionales! Para ello tenemos las **estructuras de control de flujos** 🧠⚙️

---

### ⚖️ Operadores de comparación

| Operador | Significado | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `==` | Igual que | `5 == 5` | ✅ True |
| `!=` | Distinto que | `5 != 3` | ✅ True |
| `>` | Mayor que | `10 > 5` | ✅ True |
| `>=` | Mayor o igual que | `10 >= 10` | ✅ True |
| `<` | Menor que | `3 < 8` | ✅ True |
| `<=` | Menor o igual que | `3 <= 3` | ✅ True |


### 🧠 Operadores lógicos

| Operador | Descripción | Ejemplo | Resultado |
| :--- | :--- | :--- | :--- |
| `and` | Devuelve `True` si **ambas condiciones** son verdaderas | `edad >= 18 and esEstudiante_daw` | ✅ True si los dos son True |
| `or` | Devuelve `True` si **al menos una** se cumple | `edad > 65 or esEstudiante_daw` | ✅ True si una es True |
| `not` | Invierte el valor lógico | `not tieneEntrada` | ❌ True → False |

---

## 🧭 Condicionales

### 🧩 If/Else

En Python tenemos que tener en cuenta que la linea del **if** SIEMPRE termina con `:`, esto le dice a Python "oye aqui empieza el **bloque** de lo que debes hacer si esta condicion se cumple". 

La **indetación** dentro del if es super importante, asi que atinale al `tab` cuando le metas tus condiciones al if!!! Si no sangras bien se rompe 💀

```python
edad = 20

if edad >= 18:
    print ("Eres mayor de edad!!")
else:
    print ("tas chikito uwu no puedes pasar!!!")
```

### 🔗 ELif (vamos el else if pero python es muy cool jiji)

```python
nota = 7

if nota == 10:
    print("boh, fieroteeee!!")
elif nota >= 6:
    print("not bad")
elif nota == 5:
    print("por los pelosssss")
else:
    print("palmaste colega :c")
```

---

## 🔁 Bucles

Nos permiten recorrer un trozo de código varias veces sin tener que escribirlo 40 veces. Python **no** tiene ni do...while ni switch! Por que? Porque con un while true y un break tienes un do while, y con el switch pues... tenemos un analogo! Ahora lo vemos ;D

⚠️ Cuidado con los bucles infinitos!! SIEMPRE rompe el bucle o metele algo dentro que haga que la condicion termine en algun punto!!

- `Break`: Rompe el bucle por completo y se sale, sin importar nada más!
- `Continue`: No rompe el bucle, pero se salta todo lo que queda de la iteracion y pasa directamente a la siguiente.

### 🌀 While

Mientras x condición se cumple, haz tal cosa. 

```python
contador = 1

while contador <= 5:
    print(f"El contador vale: {contador}")
    contador += 1

print("El bucle while ha terminado!")
```

### 🔀 For

En Python, `for` **no** es un contador, está diseñado para recorrer colecciones (listas, textos, etc) uno por uno, es como el `for each` o `for in` en otros lenguajes ;3. Para cada elemento que haya en esta coleccion, haz tal cosa.

```python
lstInvitados = ["Sahoro", "Gemma", "Anastasio", "Alisa Melano"]

for nombre in lstInvitados:
    print(f"Bienvenide mi estimade {nombre}")

print("Lista finalizada")
```

#### 🔢 Range

Para repetir un numero determinado de veces algo usamos `range(n)`!

```python
for numero in range(5):
    print(f"Repeticion del numero {numero}")
```

### 🧍 Structural Pattern Matching (match...case)

El **análogo del switch** pero mejoradisimo!!!

```python
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
```

> 👉 Puedes ojear el [código](./controlFlujo.py), bajarlo, probarlo... yatusae ;D