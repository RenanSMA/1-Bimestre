# Calculador de Área de Formas Geométricas.





print("1. Quadrado")
print("2. Retângulo")
print("3. Triângulo")
print("4. Círculo")

formaG = input("Digite a forma geométrica desejada para calcular a Área: ")

# Quadrado
if formaG == "1" or formaG == "Quadrado":
  lado1: float
  lado1 = float(input("Digite o valor de um do lado do Quadrado: "))
  print("A Área do Quadrado é: ", lado1 * lado1 )

# Retângulo
elif formaG == "2" or formaG == "Retângulo":
  lado1: float
  lado2: float
  lado1 = float(input("Digite um lado do Retângulo: "))
  lado2 = float(input("Digite o outro lado do Retãngulo: "))
  print("A Área do Retângulo é: ", lado1 * lado2)

# Triângulo
elif formaG == "3" or formaG == "Triângulo":
  base: float
  altura: float
  base = float(input("Digite a base do Triângulo: "))
  altura = float(input("Digite a altura do Triângulo: "))
  print("A Área do Triângulo é: ", (base * altura) / 2 )

# Círculo
elif formaG == "4" or formaG == "Círculo":
  raio: float
  raio = float(input("Digite o raio do Círculo: "))
  print("A Área do Círculo é aproximadamente: ", 3.14 * (raio ** raio))
else:
  print("Dados inválidos, tente novamente.")
  print(" ")

print("Fim do Algoritmo.")

