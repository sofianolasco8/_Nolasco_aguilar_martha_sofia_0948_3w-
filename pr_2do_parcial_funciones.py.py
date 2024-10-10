def mayor_de_tres(num1, num2, num3):
    """Devuelve el mayor de tres números."""
    return max(num1, num2, num3)

if __name__ == "__main__":
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        numero3 = float(input("Introduce el tercer número: "))
        
        mayor = mayor_de_tres(numero1, numero2, numero3)
        print(f"El mayor de los tres números es: {mayor}")
        
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")