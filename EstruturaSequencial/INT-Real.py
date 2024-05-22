numeroInt1: int
numeroInt2: int

numeroReal: float

numeroInt1 = int(input("Digite o primeiro número inteiro: "))
numeroInt2 = int(input("Digite o segundo número inteiro: "))
numeroReal = float(input("Digite um número Real: "))

# A. O produto do dobro do primeiro com metade do segundo .
print("O produto do dobro do primeiro com metade do segundo é: ", (numeroInt1 * 2) + (numeroInt2 / 2))

# B. A soma do triplo do primeiro com o terceiro.
print("A soma do triplo do primeiro com o terceiro é: ", (numeroInt1 * 3) + numeroReal)

# C. O terceiro elevado ao cubo.
print("O terceiro elevado ao cubo é: ", numeroReal ** 3)
