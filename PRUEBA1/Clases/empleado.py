from persona import Persona
class Empleado(Persona):
    def __init__(self, puesto, salario, nombre, edad):
        super().__init__(nombre, edad)
        self.puesto=puesto
        self.salario=salario
    
    def mostrar_datos(self):
        return f"""
Nombre del empleado: {self.nombre}
Edad del empleado: {self.edad}
Puesto del empleado: {self.puesto}
Salario del empleado: {self.salario}
"""