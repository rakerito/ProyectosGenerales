from fastapi import FastAPI, Path, Query
import rutas
from fastapi.exceptions import RequestValidationError
from exceptions import validation_exception_handler

app=FastAPI()
#MANEJO DE ERRORES
app.add_exception_handler(RequestValidationError, validation_exception_handler)
#RUTAS
app.include_router(rutas.router)

