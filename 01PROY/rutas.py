
from fastapi import APIRouter,Path, Query

router = APIRouter()

@router.get("/")
def inicio():
    return{"saludos": "Hola mundo con FastApi"}

#Petición con parameters (Path)
#http://localhost:8000/suma1/10/20
@router.get("/suma1/{num1}/{num2}")
def suma1(num1, num2):
    suma = int(num1) + int(num2)
    return {"suma":f"{suma}"}

#Petición con parametros (Query)
#http://localhost:8000/suma2?num1=10&num2=20
@router.get("/suma2")
def suma2(num1, num2):
    suma = int(num1) + int(num2)
    return {"suma":f"{suma}"}


#Petición de parametros(PATH) y validación de tipos
#http://localhost:8000/saludo1/Einstein/50
@router.get("/saludo1/{nombre}/{edad}")
def saludo1(nombre:str, edad:int):
    frase = f"Tu nombre es {nombre} y tu edad es: {edad}"
    return {"Saludo": f"{frase}"}

#Petición de parametros(QUERY) y validación de tipos
#http://localhost:8000/saludo2?nombre=Einstein&edad=50
@router.get("/saludo2")
def saludo2(nombre:str, edad:int):
    frase = f"Tu nombre es {nombre} y tu edad es: {edad}"
    return {"Saludo": f"{frase}"}

#Petición de parametros(PATH) validación de tipos y valores por default
#http://localhost:8000/frase1/buenos%20dias
#http://localhost:8000/frase1
# @router.get("/frase1")
# @router.get("/frase1/{saludo}")
# def frase1(saludo:str = "Hola"):
#     return {"Frase":f"{saludo}"}

@router.get("/frase1")
def frase1():
    return {"Frase":"Hola"}

@router.get("/frase1/{saludo}")
def frase2(saludo:str = "Hola"):
    return {"Frase":f"{saludo}"}


#Petición de parametros(QUERY) validación de tipos y valores por default
#http://localhost:8000/frase3?saludo=buenos%20dias
#http://localhost:8000/frase3
@router.get("/frase3")
def frase3(saludo:str = "Hola"):
    return {"Frase":f"{saludo}"}

#Petición con parametros (PATH) validación de tipo y en los valores definidos
#Multiplicar dos números entre uno y 10
#http://localhost:8000/multiplicación1/5/3
#http://localhost:8000/multiplicación1/15/3
#http://localhost:8000/multiplicación1/7
@router.get("/multiplicación1/{num1}/{num2}", name="multiplicacion1_1_10")
def multiplicacion1(
        #El primer parametro indica valor por defecto, si no hay escribir ...
        #2do indica una regla
        #3ro indica otra regla
        #4to es un texto cuando se optiene un error y es para la documentación
        #REGLAS del 2do y 3er parametro
        #gt greater than - mayor que
        #ge greater than or equal than - Mayor o igual que
        #lt less than - menor que
        #le less or equal than - Menor o igual que
        #multiple_of - Multiplo de
        #min-length - minimo de caracteres
        #max-length - Maximo de caracteres
        #regex - expresión regular
        num1:int = Path(..., ge=1, le=10, description="Primer numero de la multiplicación"),
        num2:int = Path(..., ge=1, le=10, description="Segundo numero de la multiplicación"),
    ):
    mult = num1 * num2
    return {"Multiplicación":f"{mult}"}

#Petición con parametros (QUERY) validación de tipo y en los valores definidos
#Multiplicar dos números entre uno y 10
#http://localhost:8000/multiplicación2?num1=5&num2=3
#http://localhost:8000/multiplicación2?num1=15&num2=3
#http://localhost:8000/multiplicación2?num1=3
@router.get("/multiplicación2")
def multplicacion2(
    num1:int=Query(1, ge=1, le=10, description="Primer numero de la multiplicación"),
    num2:int=Query(1, ge=1, le=10, description="Segundo numero de la multiplicación")
):
    mult = num1 * num2
    return {"Multiplicación":f"{mult}"}