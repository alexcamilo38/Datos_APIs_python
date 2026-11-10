def  dividir_seguro(a, b):
    try:
        resultado= a / b
        return resultado
    except ValueError:
        print("No se puede dividir entre cero")
        return None

print("Resultado de la primera divicion: ", dividir_seguro(10,3))
print("Resultado de la segunta divicion: ", dividir_seguro(15,8))