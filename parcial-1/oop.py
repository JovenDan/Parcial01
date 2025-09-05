#AI-TRAP:OOP
# Este ejercicio representa el modelado de personas y empleados, útil en sistemas de gestión de recursos humanos o nómina.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        if self.edad >= 18:
            return True
        return False

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        
        self.nombre = nombre
        #añadido ya que no estaban contenido en la clase
        
        self.edad = edad    
        #añadido ya que no estaban contenido en la clase
        
        self.salario = salario

Empleado_1 = Empleado("Gabriela", 25, 450000)
#Prueba de creación de objeto

print(Empleado_1.nombre, "tiene", Empleado_1.edad, "años, y gana", Empleado_1.salario, "pesos")
#Prueba de imprimir los datos del objeto