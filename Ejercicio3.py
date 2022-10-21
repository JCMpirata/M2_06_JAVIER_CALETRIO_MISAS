def imc(peso, alturaEnMetros):
  peso = float(input("Introduzca su peso en Kg: "))
  alturaEnCm = int(input("Introduzca su altura en cm: "))
  alturaEnMetros = alturaEnCm / 100
  imc = peso / (alturaEnMetros**2)
  print("El imc suyo es: ", imc)

  if imc < 18.50:
    print("Bajo peso")
  elif imc >= 18.50 and imc < 25:
    print("Normal")
  elif imc >= 25 and imc < 30:
    print("Sobrepeso")
  else:
    print("Obesidad")
    
    return imc

