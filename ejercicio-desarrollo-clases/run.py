# se importa la informacion de los dos paquetes 
from archivos.miarchivo import MiArchivo, MiArchivoEscribir# se importa las clases especificas
from mipaquete.mimodelo import Estudiante# se importa la clase estudiante

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion() # das valores a la lista
lista = [l.split("|") for l in lista] # separas en nuevas listas la informacion

# print(lista)

lista = lista[1:]
# se itera la lista 
for d in lista:
    # print(d)
    p = Estudiante(d[0], d[1], d[2], d[3]) # se crea un objeto tipo estudiante 
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo() # se entra a el metodo para cerra 
m2.cerrar_archivo() # se entra a el metodo para cerrar el segundo archivo
