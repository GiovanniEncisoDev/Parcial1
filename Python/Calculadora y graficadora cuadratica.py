#Calculadora para resolver y gráfica ecuaciones cuadráticas Alfredo Giovanni Enciso Solis 20100192
from numpy import sqrt
from sympy import *
from sympy.plotting import *
#ax^2 + bx + x = 0 forma estándar ecuación cuadrática

def raices(a,b,c):
  D = sqrt(b**2-4*a*c) #D= determinante / potencia o cuadrado D = sqrt(b**2-4*a*c) 
#Formula completa ↓
  x1 = (-b + D)/(2*a)
  x2 = (-b - D)/(2*a)
  print("La primer raíz es:",x1) #Imprime/muestra mensaje
  print("La segunda raíz es:",x2)

#Graficacion ↓
def grafica(a,b,c):
  x = Symbol('x')
  plot(a*x**2 + b*x + c)
  
if __name__ == "__main__":
  while True:
    print("Bienvenid@ a la calculadora y graficadora de ecuaciones cuadráticas")
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    c = int(input("Ingrese el valor de c: "))
    raices(float(a),float(b),float(c))
    grafica(float(a),float(b),float(c))
    
    finalizado = input("¿Quieres resolver otra ecuación cuadrática? (S/N): ")
    if finalizado == "n":
      print("Que la fuerza te acompañe")
      break