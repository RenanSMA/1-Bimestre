numeroInt1 = float
numeroInt2 = float
numeroReal = float

# 1. Resultado da Multiplicação do Primeiro com metade do Segundo
numeroInt1 = float(input("Informe o Primeiro Número Inteiro: "))
numeroInt2 = float(input("Informe o Segundo Número Inteiro: "))

resultado1 = float(numeroInt1 * 2 + numeroInt2 / 2)

print("1. O resultado é: ", resultado1)

# 2. A soma do triplo do primeiro com o terceiro número (numeroReal) 
numeroInt1 = float(input("Informe o Primeiro Número: "))
numeroReal = float(input("Informe o Terceiro Número: "))

resultado2 = float((numeroInt1 * 3) + numeroReal)

print("2. O resultado é: ", resultado2)

# 3. Número Real elevado a 3
numeroReal = float(input("Informe o número: "))

resultado3 = float(numeroReal ** 3)

print("3. O resultado é: ", resultado3)

# 4. A Raiz Cúbica do Segundo (numeroInt2)
numeroInt2 = float(input("Informe o número desejado: "))

resultado4 = float(numeroInt2 ** (1 / 3) )

print("4. A raiz cúbica é: ", resultado4)