class misDatos:

    def __init__(self,carne,nombre):

        self.carne=carne
        self.nombre=nombre

    def dump(self):

        return{
        'carne': self.carne,
        'nombre':self.nombre
        }