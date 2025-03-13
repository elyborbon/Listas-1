list = []
while True:
    palabra = input ("Escribe palabra de la lista: ")
    if palabra.lower() == "salir":
        break
    list.append(palabra)
    print (list)