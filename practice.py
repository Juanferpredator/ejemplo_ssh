#first line of code in python
print("Hello World, I am Juan Fernando Rojas from palmira.")
class perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    def Ladrar(self):
        print("guauuu")
        
    def comer(self):
        print("ñam ñam")
        
perro1 = perro("boky", 4, "labrador")
perro2 = perro("rocky", 2, "pastor aleman")
print(perro1.nombre)
print(perro2.nombre)
perro1.Ladrar()
perro2.comer()