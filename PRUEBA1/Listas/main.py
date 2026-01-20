print("Hola mundo")
a=["Hola"]
#MODIFICAR LISTAS
a[0]="Hello"
print(a)
a.append("Bon jorno")#Agrega al final de la lista
print(a)
a.insert(1,"hola")
print(a)

#BORRAR UN ELEMENTO DE LA LISTA
a.pop()#Elimina el último elemento de la lista
print(a)
#a.remove("buenos días") #Borra el elemento que pasamos como parámetro
print(a)
a.clear()#Borra todos los elementos, pero no la lista
print(a)

#FUNCIONES 
a=["Buenos días","Nice day","Bon jorno", "Bon jorno"]
print(a)
#CONTAR UN ELEMENTO DE LA LISTA
print(a.count("Bon jorno"))
#CONTAR LOS ELEMENTOS DE LA LISTA
print(len(a))
#EN QUE PISICIÓN ESTÁ UN ELEMENTO
print(a.index("Nice day"))
#ORDENAR DATOS NÚMERICOS
a=[8,5,3,10]
print(a)
