# IMC: massa / (altura ** 2)

massa: float
alutra: float

massa = float(input("Informe a massa: "))
altura = float(input("Informe a altura: "))

imc = massa / (altura ** 2)

if imc < 18.5:
  print("Seu IMC se classica como Magreza: ", imc)
else:
  # imc >= 18.5
  # Normal, Sobrepeso I, Obesidade II, Obesividade Grave III
  if imc >= 18.5 and imc < 25.0:
    print("Seu IMC se classifica como Normal: ", imc)
  else:
    # imc >= 25
    # Sobrepeso I, Obesidade II, Obesividade Grave III
    if imc >= 25.0 and imc < 30.0:
      print("Seu IMC se classifica como Sobrepeso I: ", imc)
    else:
      # >=
      # Obesidade II, Obesividade Grave III
      if imc >= 30.0 and imc < 40.0:
        print("Seu IMC se classifica como Obesidade II: ", imc)
      else:
        print("Seu IMC se classifica como Obesidade III: ", imc)

print("Fim.")
