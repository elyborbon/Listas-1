#Recorrer varias listas a la vez 

Nombre = ["Ana", "Eduardo", "Maria", "Sebastian "]
edad = [12, 13, 14, 15]
ciudades = ["Estados Unidos", "Mexico", "Alemania", "España"]

for elemento in zip(Nombre, edad, ciudades):
    print (elemento)
    