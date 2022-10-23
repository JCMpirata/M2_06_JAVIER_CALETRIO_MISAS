#Ejercicio 3
#Creo la funcion lee_numero para pedir un numero, la cual la utilzo para pedirle tres numeros al usuario. Luego, en la funcion mayor introduzco los tres numeros en una lista y los ordeno de mayor a menor.
def lee_numero():
  numero = int(input("Introduzca un numero: "))
  return numero

num1 = lee_numero()
num2 = lee_numero()
num3 = lee_numero()

def mayor():
  numeros = [num1, num2, num3]
  numeros.sort(reverse = True)
  return numeros

  
  

               