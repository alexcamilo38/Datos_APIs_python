import json

class CarritoCompras:

    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)

    def cargar(self, archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            self.productos = json.load(f)

carrito1 = CarritoCompras()
carrito1.agregar("Camisa")
carrito1.agregar("Pantalón")
carrito1.guardar("carrito.json")

carrito2 = CarritoCompras()
carrito2.cargar("carrito.json")
print("productos del segundo carrito:")
print(carrito2.productos)