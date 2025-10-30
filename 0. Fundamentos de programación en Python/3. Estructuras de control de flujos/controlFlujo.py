# CONTROL DE FLUJOS!!

# If / else

edad = 20

if edad >= 18:
    print ("Eres mayor de edad!!")
else:
    print ("tas chikito uwu no puedes pasar!!!")

# Elif

nota = 4

if nota == 10:
    print("boh, fieroteeee!!")
elif nota >= 6:
    print("not bad")
elif nota == 5:
    print("por los pelosssss")
else:
    print("palmaste colega :c")

# While

contador = 1

while contador <= 5:
    print(f"El contador vale: {contador}")
    contador += 1

print("El bucle while ha terminado!")

# For

lstInvitados = ["Sahoro", "Gemma", "Anastasio", "Alisa Melano"]

for nombre in lstInvitados:
    print(f"Bienvenide mi estimade {nombre}")

print("Lista finalizada")

# Range

for numero in range(5):
    print(f"Repeticion del numero {numero}")

# Match...case

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