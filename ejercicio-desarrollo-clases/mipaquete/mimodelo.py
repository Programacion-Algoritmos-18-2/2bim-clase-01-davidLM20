"""
    creación de clases
"""
# clase estudiante 
class Estudiante(object):
    
    # se crea parametros 
    def __init__(self, n, n1, n2, n3):# constructor
        
        self.nombre = n
        # se le dice a estos parametros para que se transformen en tipo float
        self.nota1 = float(n1) 
        self.nota2 = float(n2)
        self.nota3 = float(n3)
        self.promedio = 0.0
    # se crea los metodos para agregar el nombre  cada una de las notas y promedio
    def agregar_nombre(self, n):
        self.nombre = n

    def agregar_promedio(self, pr):
        self.promedio = pr

    def agregar_nota1(self, n1):
        self.nota1 = n1

    def agregar_nota2(self, n2):       
        self.nota2 = n2

    def agregar_nota3(self, n3):        
        self.nota3 = n3

    # se crea los metodos para obtener nombre cada una de las notas y promedio
    def obtener_nombre(self):
        return self.nombre

    def obtener_nota1(self):
        return self.nota1

    def obtener_nota2(self):
        return self.nota2
    
    def obtener_nota3(self):
        return self.nota3

    def obtener_promedio(self):    
        self.promedio = (self.nota1 + self.nota2 + self.nota3)/3 # se calcula el promedio
        return self.promedio
        
    # se crea el metodo para la impresion de archivos (str es igual a to String en Java)
    def __str__(self):
        return "%s - %.2f\n" % (self.nombre, self.obtener_promedio())
