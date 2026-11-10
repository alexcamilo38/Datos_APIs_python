try:
    with open("no_existe.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")