print(" ")
print("nolasco_aguilar_martha_sofia_0948_3w")
print(" ")
def es_vocal(caracter):#se crea una lista 

    vocales = "aeiouAEIOU"  #  vocales  minúsculas y mayúsculas
    return caracter in vocales  # imprime True si es vocal y False si no 

# indica al usuario ingresar  una letra
letra = input("Ingresa una letra ")

# Verificar si es una vocal 
if es_vocal(letra):
    print(True)#indica que  es una vocal
else:
    print(False)#IDICA QUE NO ES UNA VOCAL