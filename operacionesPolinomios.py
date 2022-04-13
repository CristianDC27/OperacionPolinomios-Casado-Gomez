"""Algortimo para la resolucion de operaciones entre 2 polinomios

Ejercicio: Resolver la siguiente multiplicación de polinomios
P(x) = 7*x**3 + 2*x**2 + x - 7
Q(x) = x**2 + 3

"""

#Importamos la libreria SympY para usar variables simbolicas (x, y)
import sympy

from operacion import Operacion

while True:
   try:
      print("Ejemplo de formato: 7*x**3 + 2*x**2 + x - 7\n")
      #Obtenes los dos polinomios introducidos por el usuario
      P1 = input("Primer Polinomio: ")
      P2 = input("Segundo Polinomio: ")

      #Definimos los simbolos
      sympy.init_printing()
      x,y = sympy.symbols('x,y')

      #Luego almacenamos en varibles los dos polinomios procesados por la funcion Poly de sympy
      Poly1 = sympy.Poly(P1)
      Poly2 = sympy.Poly(P2)

      break

   except Exception as e:
      print("Formato erróneo\n")

operacion = Operacion(Poly1, Poly2)

# Dar opcion al usuario a sumar o restar
while True:
    option = input("Introduzca la operación a realizar '+' o '-': ")
    if option == "+" or option =="-":
        break

print("Resultado: ", operacion.operar(option))