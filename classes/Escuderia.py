class Escuderia:
    def _init_(self,nombre,motor,piloto,costoanual):
        self.nombre=nombre
        self.motor=motor
        self.piloto=piloto
        self.costo=costoanual
    
    def escuderiaf1(self):
        print("nombre escuderia: ", self.nombre)  
        print("motor: ", self.motor)
        print("piloto: ", self.piloto)
        print("costo anual: ", self.costo)