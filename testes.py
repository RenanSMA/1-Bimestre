# Peso Ideal:





genero = str(input("Você é Homem ou Mulher? "))


if genero == "Homem" or genero == "H":
  altura = float(input("Qual a sua altura (em centímetros)? "))
  print("Seu Peso Ideal é ", (72.7 * altura) - 58)

elif genero == "Mulher" or genero == "M":
  altura = float(input("Qual a sua altura? "))
  print("Seu Peso Ideal é ", (62.1 * altura) - 44.7)