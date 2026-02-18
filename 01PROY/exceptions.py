from fastapi import Request #ENTREGA EL URL
from fastapi.exceptions import RequestValidationError #ENTREGA EL MENSAJE DE ERROR
from fastapi.responses import JSONResponse #PREPARAR LA RESPUESTA

MENSAJES_ERROR = {
    "multiplicacion1_1_10":{
        "num1":{
            "less_than_equal":"El primer parámetro debe ser menor a 10",
            "greater_than_equal":"El primero parámetro debe ser mayor a 1",
            "int_parsing":"El primer parámetro debe ser un número",
            "missing":"El primer parámetro es requerido"
        },
        "num2":{
            "less_than_equal":"El segundo parámetro debe ser menor a 10",
            "greater_than_equal":"El segundo parámetro debe ser mayor a 1",
            "int_parsing":"El segundo parámetro debe ser un número",
            "missing":"El segundo parámetro es requerido"
        }
    }
}

async def validation_exception_handler(request: Request, exc:RequestValidationError):
    errors=[]#SE PREPARA UNA LISTA PARA ALMACENAR TODOS LOS ERRORES
    ruta_obj=request.scope.get("route")
    ruta_name = getattr(ruta_obj, "name", None)
    for error in exc.errors():
        parametro= error["loc"][-1] #ENTREGA EL PARÁMETRO QUE FALLÓ
        tipo= error["type"]#ENTREGA EL TIPO DE ERROR (ej. greater_than_equal)

        # Normalizar el tipo para mapear con MENSAJES_ERROR
        if "not_le" in tipo or "less_than_equal" in tipo:
            tipo_key = "less_than_equal"
        elif "not_ge" in tipo or "greater_than_equal" in tipo:
            tipo_key = "greater_than_equal"
        elif "type_error" in tipo or "integer" in tipo:
            tipo_key = "int_parsing"
        elif "missing" in tipo:
            tipo_key = "missing"
        else:
            tipo_key = tipo

        ruta_dicc=MENSAJES_ERROR.get(ruta_name,{})
        parametro_dicc=ruta_dicc.get(parametro,{})
        mensaje_dicc=parametro_dicc.get(tipo_key,f"Error en el parámetro {parametro}: {tipo}")
        errors.append(mensaje_dicc)

    return JSONResponse(
        status_code=422,
        content={
            "detalles": errors
        }
    )