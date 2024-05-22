lado1: float
lado2: float
lado3: float

print("Verificador de Tipo de Triangulo.")
print(" ")

try:
  lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
except:
  lado1 = 0

try: 
  lado2 = float(input("Digite o valor do segundo lado do triângulo: "))
except:
  lado2 = 0

try:
  lado3 = float(input("Digite o valor do terceiro lado do triângulo: "))
except:
  lado3 = 0


if lado1 == 0 and lado2 == 0 and lado3 == 0:
  print("Dados inválidos, tente novamente.")
elif lado1 == lado2 and lado1 == lado3:
  print("De acordo com os dados informados, trata-se de um Triângulo Equilátero.")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("De acordo com os dados informados, trata-se de um Triângulo Isósceles.")

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  print("De acordo com os lados informados, trata-se de um Triângulo Escaleno")  

