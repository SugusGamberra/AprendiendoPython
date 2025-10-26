# Para el paradigma funcional voy a hacer el cuadrado d euna suma

def cuadrado (num):
    return num * num

def suma (a, b):
    return a + b

resultado = cuadrado(suma(3, 4))

print("El resultado es: ", resultado)