numero1: float
numero2: float
operacao: str

print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite a opção desejada: ")

# Try Except ou Try Catch

try:
  numero1 = float(input("Digite o primeiro número: "))
except:
  print("Dado inválido, tente novamente.")

try:
  numero2 = float(input("Digite o segundo número: "))
except:
  print("Dado inválido, tente novamente.")




if operacao == "1" or operacao == "Adição":
  # Adição
  print("O Resultado da Adição é: ", numero1 + numero2)

elif operacao == "2" or operacao == "Subtração":
  # Subtração
  print("O Resultado da Subtração é: ", numero1 - numero2)

elif operacao == "3" or operacao == "Multiplicação":
  # Multiplicação
  print("O Resultado da Multiplicação é: ", numero1 * numero2)

elif operacao == "4" or operacao == "Divisão":
  print("O Resultado da Divisão é: ", numero1 / numero2)
else:
  print("Dados inválidos, tente novamente.")