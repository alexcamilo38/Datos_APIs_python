import json

inventario = [ 
{"producto": "Camisa", "precio": 45000, "stock": 20}, 
{"producto": "Gorra", "precio": 30000, "stock": 5}, 
{"producto": "Pantalón", "precio": 89000, "stock": 12}, 
{"producto": "Medias", "precio": 8000, "stock": 40}, 
{"producto": "Zapatos", "precio": 150000, "stock": 3}, 
]



print("Productos por reponer ")

for producto in inventario:
    if producto["stock"] < 10:
        print("producto:",producto["producto"])
        print("precio:",producto["precio"])
        print("Stock:",producto["stock"])

with open("inventario.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

    nuevo_producto= {
        "producto": "Bufanda",
        "precio": 25000,
        "stock": 15
    }
inventario.append(nuevo_producto)

with open("inventario.json", "w", encoding="utf-8") as f:
    json.dump(inventario, f, indent=4, ensure_ascii=False)

print("Total de productos:", len(inventario))