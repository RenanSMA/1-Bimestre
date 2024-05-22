# Renan

# Exercício 1

area: float
circunferencia: float
diametro: float

print("Informações de um círculo.")
print(" ")

raio = float(input("Digite o valor do raio do círculo: "))

# Área
area = 3.14 * (raio ** 2)
print("A área deste círculo é", area)

# Circunferência
circunferencia = (2 * 3.14) * raio
print("A circunferência deste círculo é", circunferencia)

# Diâmetro
diametro = 2 * raio
print("O diâmetro deste círculo é", diametro)
