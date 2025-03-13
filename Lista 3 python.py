lista = [1,2,3,4,5,6,7,8,9]
numeros_mult = []
numeros_mult_1 = []
numeros_mult_2 = []
numeros_mult_3 = []

for numero in lista:
   multiplicacion = numero * 2
   numeros_mult.append(multiplicacion)
   print (numeros_mult)
for numero_1 in lista:
   suma = numero_1 + 7
   numeros_mult_1.append(suma)
   print (numeros_mult_1)
for numero_3 in lista:
   resta = numero_3 -2
   numeros_mult_2.append(resta)
   print(numeros_mult_2)
#----------------------------------------------
#numeros_mult = [numero * 2 for numero in lista]
#print (numeros_mult)
   
