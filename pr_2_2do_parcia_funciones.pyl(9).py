print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")

def sum(lista):
    total = 0
    for num in lista:
        total += num  # Sumar cada número al total
    return total

def multip(lista):

    total = 1
    for num in lista:
        total *= num  # Multiplicar cada número al total
    return total

# Ejemplos de uso
print(sum([5,6,7,8]))    #devulve a 26
print(multip([ 2, 3, 4,5]))  #  devuelve a 120