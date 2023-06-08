# En Pyhton la función "raise" se utiliza para generar una excepción (error) en el programa
# En el código ValueError es el tipo de excepción, sin embargo esta puede variar según nosotros lo determinemos.

edad = int(input("Ingrese edad:\n"))

if edad < 0:
    raise ValueError("La edad no puede ser negativa")

# Cabe destacar que hay que manejar esta función con mucho cuidado, ya que se genera un error en el programa y se recomienda hacer uso de la dunción try/exception para que le programa no se caiga y poder atrapar estos errores.
