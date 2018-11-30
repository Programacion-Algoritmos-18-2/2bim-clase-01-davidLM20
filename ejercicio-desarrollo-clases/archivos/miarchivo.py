
import codecs # se importa libreria codex 

class MiArchivo: # se crea la clase archivo 
    
    # se crea el metodo para el parametro 
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r") #se le dice que archivo debe leer
    # se cree el metodo para que lea el archivo
    def obtener_informacion(self):
        return self.archivo.readlines() # debe leer linea por linea
    # se crea un metodo para cerrar el archivo 
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir: # se crea una nueva clase p para escribir el archivo
    """
    """
    
    def __init__(self): #  crea el metodo para el parametro 
        """
        """
        self.archivo = codecs.open("data/final.csv", "a") # se le dice en que archivo se debe escribir 

    def agregar_informacion(self, p):
        self.archivo.write("%s-%.2f\n" % (p.nombre, p.promedio)) # se agrega la informacion que se escribira en el archivo
    # se crea el metodo que debe cerrar el archivo 
    def cerrar_archivo(self):
        self.archivo.close()
