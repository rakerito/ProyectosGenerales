#DICCIONARIOS
#CREAR Y MOSTRAR UN DICCIONAIO
a={}
print(a)
#CLAVE:VALOR
a={
    "Nombre":"Einstein",
    "Edad": 70,
    "Domicilio":"Av. La palma",
    "Telefono":"4141234390"
}
print(a)

#MODIFICAR UN VALOR DEL DICCIONARIO
a["Edad"]=60
print(a)
print(a["Nombre"])

#BORRAR UN ELEMENTO DEL DICCIONARIO
del a["Edad"]
print(a)
a.pop("Nombre")
a.popitem()
print(a)

#AGREGAR UN ELEMENTO DEL DICICONARIO
a["Titulo"]="Ing. en Física"
print(a)

a={
    "Nombre":"Einstein",
    "Edad": 70,
    "Domicilio":"Av. La palma",
    "Telefono":"4141234390"
}

# print(a.keys())
# print(a.values())
# print(a.items())

for clave in a.keys():
    print(clave)

for valor in a.values():
    print(valor)

for clave, valor in a.items():
    print(clave , " : " , valor)


b=[{
    "Nombre":"Einstein",
    "Edad": 70,
    "Domicilio":"Av. La palma",
    "Telefono":["4141234393", "4141234391","4141234392"]
},
{
    "Nombre":"Newton",
    "Edad": 50,
    "Domicilio":"Av. La palma",
    "Telefono":"4141235390"
},{
    "Nombre":"Pascal",
    "Edad": 60,
    "Domicilio":"Av. La palma",
    "Telefono":"4141234391"
},
]

print(b)

#ACTIVIDAD

# AGREGAR UN DICCIONARIO MÁS A LA LISTA
b.append({
    "Nombre":"Galileo",
    "Edad": 78,
    "Domicilio":"Av. Italia",
    "Telefono":"4149876543"
})

print("AGREGAR UN DICCIONARIO MÁS A LA LISTA")
print(b)


# AGREGAR UN ELEMENTO A NEWTON
b[1]["Titulo"] = "Físico y Matemático"

print("AGREGAR UN ELEMENTO A NEWTON: ")
print(b[1])
print("")

# BORRAR EL ÚLTIMO ELEMENTO DEL ARREGLO
b.pop()
print("")
print("BORRAR EL ÚLTIMO ELEMENTO DEL ARREGLO:")
print(b)
print("")

# MODIFICAR LA EDAD DE EINSTEIN
b[0]["Edad"] = 99

print("MODIFICAR LA EDAD DE EINSTEIN:")
print(b[0])
print("")

# MOSTRAR EL SEGUNDO TELÉFONO DE EINSTEIN
print("MOSTRAR EL SEGUNDO TELÉFONO DE EINSTEIN")
print(b[0]["Telefono"][1])

