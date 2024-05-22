# Renan

# Exercício 3

categoria: str
preco: float
desconto: float
precoFinal: float

print("Desconto com base na Categoria.")
print(" ")

categoria = str(input("Qual a categoria do produto? (A, B ou C?) "))
print("A categoria informada foi", categoria)
print(" ")

preco = float(input("Qual o preço do produto? "))


# Categoria A
if categoria == "A" or  categoria == "a":
  desconto = preco * 0.10
  precoFinal = preco - desconto
  print("Você tem direito a um desconto de 10%")
  print("Valor final com desconto:", precoFinal)

# Categoria B
elif categoria == "B" or categoria == "b":
  desconto = preco * 0.15
  precoFinal = preco - desconto
  print("Você tem direito a um desconto de 15%")
  print("Valor final com desconto:", precoFinal)

# Categoria C
elif categoria == "C" or categoria == "c":
  desconto = preco * 0.20
  precoFinal = preco - desconto
  print("Você tem direito a um desconto de 20%")
  print("Valor final com desconto:", precoFinal)

