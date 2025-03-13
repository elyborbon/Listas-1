usuarios = [
    {"nombre": "Juan", "edad": 13, "estado": "Activo"}, 
    {"nombre": "Ely", "edad": 20, "estado": "Activo"}, 
    {"nombre": "Juan", "edad": 18, "estado": "Inactivo"}, 
    {"nombre": "Maria", "edad": 29, "estado": "Activo"}, 
    {"nombre": "Pedro", "edad": 45, "estado": "Activo"}
    ]
#Filtrar datos usando un ciclo For
result = []
for item in usuarios:
    if (item["edad"] > 43 and item ["estado"]=="Activo"):
        result.append(item)
        print (result)
    #print (item)