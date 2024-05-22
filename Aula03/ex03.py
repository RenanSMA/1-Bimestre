# Calculadora de Múltipla Escolha.

numero1: int
numero2: int
operacao: str

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Você gostaria de somar (1) ou subtrair (2)? ")

if operacao == "Soma" :
  soma: int = numero1 + numero2
  print(numero1, "+", numero2, "=", soma)
else 
  if operacao == "Sub" :
    sub: int = numero1 - numero2
    print(numero1, "-", numero2, "=", sub)

  else:
    print("Dados incorretos, tente novamente.")    