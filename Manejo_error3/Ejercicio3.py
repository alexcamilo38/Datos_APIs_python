while True:
    try:
        numero = float(input("Ingrese un Número: "))
        
        break
    except ValueError:
        print("Error debe inresar un numero valido")
print("El numero ingresado es: ",numero)


