# Renan

# Exercício 2

num: int

print("Verificador de número Positivo, Zero ou Negativo")
print(" ")

num = int(input("Digite um número inteiro: "))


# Caso Positivo
if num > 0:
  print("O número informado foi", num)
  print("Este se trata de um número positivo")

# Caso 0
elif num == 0:
  print("O número informado foi", num)
  print("Ou seja, 0")
  
# Caso Negativo
elif num < 0:
  print("O número informado foi", num)
  print("Este se trata de um número negativo")
