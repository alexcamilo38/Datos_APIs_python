ventas = [45000, 120000, 8000, 300000]

with open("ventas.txt", "w", encoding="utf-8") as f:
    for venta in ventas:
        f.write(str(venta) + "\n")

    total = 0
with open("ventas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        valor = int(linea.strip())
        total = total + valor

# Mostrar el resultado
print("Registro de ventas")
print("Total de las ventas:", total)

