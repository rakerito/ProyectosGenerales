from fastapi import APIRouter, Path, Query
from uuid import UUID
from app.services.productos_service import list_products, get_products, create_product, update_product, delete_product
from app.models.producto import ProductCreate, ProductUpdate, ProductOut, ProductList

router = APIRouter(prefix="/productos")

# Mostrar un listado de varios productos (máx. 200, por defecto 100)
# Ejemplos:
# http://localhost:8000/productos?limit=100&offset=0
# http://localhost:8000/productos?limit=100&offset=10

@router.get("/", name="lista_productos")
def listar_productos(limit: int = Query(100, ge=1, le=200), offset: int = Query(0, ge=0)):
    return list_products(limit=limit, offset=offset)

@router.get("/{product_id}", response_model=ProductOut, name="obtener_un_producto_por_ID")
def api_get_product(product_id: UUID = Path(...)):
    return get_products(product_id)

@router.post(
    "/",
    response_model=ProductOut,
    name="crear_producto",
    responses={
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "name"],
                                "msg": "field required",
                                "type": "value_error.missing"
                            }
                        ]
                    }
                }
            }
        },
        500: {
            "description": "Server Error",
            "content": {
                "application/json": {
                    "example": {"detail": "Error al insertar el nuevo registro: ..."}
                }
            }
        }
    },
)
def api_create_product(body: ProductCreate):
    # Aquí devolvemos directamente el objeto, no envuelto en {"Item": ...}
    return create_product(body.model_dump())

@router.put("/{product_id}", response_model=ProductOut, name="actualizar_producto")
def api_update_product(product_id: UUID, body: ProductUpdate):
    return update_product(product_id, body.model_dump(exclude_none=True))

@router.delete("/{product_id}", name="eliminar_producto")
def api_delete_product(product_id: UUID):
    return delete_product(product_id)
