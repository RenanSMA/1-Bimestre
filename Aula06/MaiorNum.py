print("Digite três números:")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

# PARTE 1: Encontrando o maior número
if num1 >= num2 and num1 >= num3:
  maior = num1
elif num2 >= num1 and num2 >= num3:
  maior = num2
else:
  maior = num3

print("O maior número é:", maior)

# PARTE 2: Ordenando os números em ordem crescente

# Comparando N1
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        central = num2
        maior = num3
    else:
        central = num3
        maior = num2

# Comparando N2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        central = num1
        maior = num3
    else:
        central = num3
        maior = num1

# Quando N3 for maior
else:
    menor = num3
    if num1 <= num2:
        central = num1
        maior = num2
    else:
        central = num2
        maior = num1

print("Os números em ordem crescente são:", menor, central, maior)
