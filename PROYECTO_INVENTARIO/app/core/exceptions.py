from fastapi import Request # Entrega el URL
from fastapi.exceptions import RequestValidationError # Entrega el mensaje de error
from fastapi.responses import JSONResponse # Preparar la respuesta

MNESAJES_ERROR = {
    "lista_productos":{
        "limit":{
            "less_than_equal":"El limite debe ser menor o igual a 200",
            "greater_than_equal":"El limite debe ser mayor o igual a 0",
            "int_parsing":"El limite debe ser un número"
        },
        "offset":{
            "greater_than_equal":"El offset debe ser mayor o igual a 0",
            "int_parsing":"El offset debe ser un número"
        }
    },
    "crear_producto":{
        "name":{
            "missing":"El campo 'name' es obligatorio",
        },
        "quantity":{
            "missing":"El campo 'quantity' es obligatorio",
            "int_parsing":"El campo 'quantity' debe ser un número"
        },
        "ingreso_date":{
            "missing":"El campo 'ingreso_date' es obligatorio",
        },
        "min_stock":{
            "greater_than_equal":"El stock mínimo debe ser mayor o igual a 0",
            "missing":"El campo 'min_stock' es obligatorio",
        },
        "max_stock":{
            "greater_than_equal":"El stock máximo debe ser mayor o igual a 0",
            "less_than_equal":"El stock máximo debe ser menor o igual a 1000",
            "missing":"El campo 'min_stock' es obligatorio",
        }
    },
    "Obtener_un_producto_por_ID":{
        "product_id":{
            "uuid_parsing":"Tiene que ser un ID de tipo UUID",
            "missing":"El campo Id del Producto es obligatorio",
        }
    },
    "actualizar_producto":{
        "product_id":{
            "uuid_parsing":"Tiene que ser un ID de tipo UUID",
            "missing":"El campo Id del Producto es obligatorio",
        }
    },
    "eliminar_producto":{
        "product_id":{
            "uuid_parsing":"Tiene que ser un ID de tipo UUID",
            "missing":"El campo Id del Producto es obligatorio",
        }
    }
}

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = [] # Se prepara una lista para almacenar todos los errores
    ruta_obj = request.scope.get("route") # Se obtiene la ruta del request
    #print(ruta_obj)
    ruta_name = getattr(ruta_obj, "name", "") # Se obtiene el nombre de la ruta
    print(ruta_obj)
    print (exc.errors())
    for error in exc.errors():
        parametro = error["loc"][-1] 
        tipo = error["type"]
        #print(parametro)
        #print(tipo)
        ruta_dicc = MNESAJES_ERROR.get(ruta_name, {})
        parametro_dicc = ruta_dicc.get(parametro, {})
        mensaje_dicc = parametro_dicc.get(tipo, f"Error en el parametro {parametro}")
        errores.append(mensaje_dicc)

    return JSONResponse(
        status_code=422, # en la validacion de la informacion es 422
        content={
            "detalles": errores
        }
    )