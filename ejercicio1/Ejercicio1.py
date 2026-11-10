estudiantes = ["Carlos", "Ana", "Luis"]

with open("estudiantes.txt", "w", encoding="utf-8") as f:
    for nombre in estudiantes:
        f.write(nombre + "\n")
with open("estudiantes.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        print(i, linea.strip())

with open("estudiantes.txt", "a", encoding="utf-8") as f:
    f.write("Marta\n")
