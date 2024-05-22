# Programa de IMC v2
# IMC: massa / (altura ** 2)
# Em python "else if" é elif

"(Por enquanto) Obrigatoriamente ele executa apenas a primeira condição Verdadeira. Ele vai parar somente na primeira que ele encontrar que seja Verdadeira, não importa se as outras condições também forem verdadeiras."

massa: float
alutra: float

massa = float(input("Informe a massa: "))
altura = float(input("Informe a altura: "))

imc = massa / (altura ** 2)

if imc < 18.5:   # apenas números < 18.5
  # 1
  print("Seu IMC se classifica como Magreza: ", imc)
elif imc < 25.0:   # apenas números < 25.0
  # 2 
  print("Seu IMC se classifica como Normal: ", imc)
elif imc < 30.0:
  # 3
  print("Seu IMC se classifica como Sobrepeso I: ", imc)
elif imc < 40.0:
  # 4  
  print("Seu IMC se classifica como Obesidade II: ", imc)
else: 
  # 5
  print("Seu IMC se classifica como Obesidade III: ", imc)

print("Fim.")