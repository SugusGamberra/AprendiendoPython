# Un ejemplo de intérprete usando Python sería...
# Renombrar archivos de tu PC
# Crearé una archivo dentro de mi proyecto con un .txt que inicialmente se llamará "abc.txt"
# y pasaremos a llamarlo "def.txt"

import os

carpeta = r"C:\Users\sugus\PyCharmMiscProject\3. EjemploInterpreteRenombrarArchivos"
archivo_original = "abc.txt"
nuevo_nombre = "def.txt"

os.rename(os.path.join(carpeta, archivo_original), os.path.join(carpeta, nuevo_nombre))
print(f"{archivo_original} -> {nuevo_nombre}")

    # El intérprete de Python lee el código línea por línea y ejecuta al momento
    # Si hay un error como que no existe el directorio se detiene en esa línea y muestra el error
    # Si quieres hacer la prueba tan solo tienes que modificar carpeta=r"C:\......" con tu carpeta de prueba
    # El archivo que quieras renombrar, le pones su nombre actual en archivo_original
    # Y el nombre que le quieras dar se lo pones en nuevo_nombre