print(" ")
print("nolasco_aguilar_martha_sofia")
def distancia_dirigida(punto1, punto2):
    """Devuelve la distancia dirigida entre dos puntos."""
    return (punto2[0] - punto1[0], punto2[1] - punto1[1])

if __name__ == "__main__":
    try:
        x1 = float(input("Introduce la coordenada x del primer punto: "))
        y1 = float(input("Introduce la coordenada y del primer punto: "))
        x2 = float(input("Introduce la coordenada x del segundo punto: "))
        y2 = float(input("Introduce la coordenada y del segundo punto: "))
        
        punto1 = (x1, y1)
        punto2 = (x2, y2)
        
        distancia = distancia_dirigida(punto1, punto2)
        print(f"La distancia dirigida entre {punto1} y {punto2} es: {distancia}")
        
    except ValueError:
        print("Entrada no válida. Por favor, introduce números.")