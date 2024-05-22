# Renan

# Exercício 4

num1: float
num2: float
num3: float

print("Verificador de Valor Central entre três Números Diferentes.")
print(" ")

num1 = float(input("Digite o primeiro número: "))
print("Seu primeiro digito foi", num1)
print(" ")

num2 = float(input("Digite o segundo número: "))
print("Seu segundo digito foi", num2)
print(" ")

num3 = float(input("Digite o terceiro número: "))
print("Seu terceiro digito foi", num3)
print(" ")

# Caso onde N1 é o meio:
if (num1 > num2 and num1 < num3) or num1 > num3 and num1 < num2:  
  print("O Valor Central foi o primeiro, ou seja,", num1)


# Caso onde N2 é o meio:
elif (num2 > num1 and num2 < num3) or num1 > num2 and num3 < num2:
  print("O Valor Central foi o segundo, ou seja,", num2)

# Caso onde N3 é o meio:
elif (num3 > num1 and num3 < num2) or num1 > num3 and num3 > num2:
  print("O Valor Central foi o terceiro, ou seja,", num3)



