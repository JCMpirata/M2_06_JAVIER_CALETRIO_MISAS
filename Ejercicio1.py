#Ejercicio 1
# Utilzo el modulo math para poder utilzar el numero pi, con math.pi
# Luego, creo la funcion, solicito al usuario el radio de la circunferencia y calculo el area con la formula.
import math
def area_circulo():
  radio = int(input("Introduce el radio del circulo: "))
  area = math.pi * (radio * radio)
  print("El area del ciculo es: ", area)
  return radio