altura: float
genero: str

print("Para iniciar, é necessário responder a seguinte questão:")

try:
  genero = str(input("Você é Homem ou Mulher? "))
except:
  print("Dados inválidos, tente novamente.")  


if genero == "Homem" or genero == "H":
  try:
    altura = float(input("Informe sua altura: "))
    print("Seu peso ideal corresponde à", (72.7 * altura) - 58)
  except:
    print("Dados inválidos, tente novamente.")

elif genero == "Mulher" or genero == "M":
  try:
    altura = float(input("Informe sua altura: "))
    print("Seu peso ideal corresponde à", (62.1 * altura) - 44.7)
  except:
    print("Dados inválidos, tente novamente.")