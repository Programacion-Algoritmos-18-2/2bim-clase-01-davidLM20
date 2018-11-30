 # Ejemplo manejo de exepciones

try:
    numero1 = input("Ingrese el primer numero:\n")
    numero1 = int(numero1)
    numero2 = input("Ingrese el segundo numero\n")
    numero2 = int(numero2)
    operacion = numero1 / numero2
    print("el valor de la division es %d" % (operacion))
    
except NameError as e:
 	print("Existe un error: %s" % e)

except ZeroDivisionError as e:
	print("Existe un error: %s" % e)

except ValueError as e:
 	print("Existe un error (%s): %s" % (e.__class__,e))

except Exception as e:
 	print("Existe un error (%s): %s" % (e.__class__,e))