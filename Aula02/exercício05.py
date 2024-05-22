# 1. Salário Bruto
valorGanho = float
horasTrabalhadas = float
diasMes = float

valorGanho = float(input("Quanto você ganha por hora em seu trabalho? "))
horasDia = float(input("Quanto tempo(horas) você trabalha em um dia? "))
diasMes = float(input("Quantos dias você trabalha em um mês? "))
salarioBruto = valorGanho * horasDia * diasMes

print("O Salário Bruto é: ", salarioBruto)

# Descontos Separado
descontoIR = float(salarioBruto - (0.11 * salarioBruto))
print("O desconto do salário com a taxa do IR(11%) é: ", descontoIR)

descontoINSS = float(salarioBruto - (0.08 * salarioBruto))
print("O desconto do salário com a taxa do INSS(8%) é: ", descontoINSS)

descontoSindicato = float(salarioBruto - (0.05 * salarioBruto))
print("O desconto do salário com a taxa do Sindicato(5%) é: ", descontoSindicato)


# Desconto Total
descontoIR = float(salarioBruto - (0.11 * salarioBruto))

descontoINSS = float(descontoIR - (0.08 * descontoIR))

descontoSindicato = float(descontoINSS - (0.05 * descontoINSS))

print("O Salário Líquido com descontos de IR, INSS e Sindicato é: ", descontoSindicato)