print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")
def my_function(p1, p2):
    coo1, coo1 = p1
    coo2, coo2 = p2
    # Calcula la diferencia de las coordenadas 
    return (coo2 - coo1, coo2 - coo1)

# indica al usuario que ingrese las coordenadas de los puntos
print("ingesa las coordenadas del primer punto")
coo1 = float(input("coordenada 1  "))
coo1 = float(input("coordenada 2 "))
print("Ingrese las coordenadas del segundo punto:")
coo2 = float(input("coordenada 1 "))
coo2 = float(input("coordenada 2 "))

# mostrar el resultado
resultado = my_function((coo1, coo1), (coo2 , coo2))
print(f"La distancia dirigida entre los puntos es: {resultado}")