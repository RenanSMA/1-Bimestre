texto: str = "testando python"
numero1: float = 10
numero2: float = 10.5
ligado: bool = True 

#(Hashtag para Comentários!) 

primeiroNome: str = "Robô"
segundoNome: str = " Maneiro disse"
nomeCompleto: str = primeiroNome + segundoNome

print(nomeCompleto)

#------------

numero1: int
numero2: int
soma: int

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número "))
soma = numero1 + numero2
print(soma)

#------------

primeiroNumero: float = 9.0
segundoNumero: float = 3.0

resultado: float = primeiroNumero + segundoNumero
print("Soma: ", resultado)
resultado = primeiroNumero - segundoNumero
print("Subtração: ", resultado)
resultado = primeiroNumero * segundoNumero
print("Multiplicação: ", resultado)
resultado = primeiroNumero / segundoNumero
print("Divisão: ", resultado)
resultado = primeiroNumero ** segundoNumero
print("Potenciação: ", resultado)
resultado = primeiroNumero ** (1 / 2)
print("Raiz do Primeiro Número: ", resultado)
resultado = segundoNumero ** (1 / 2)
print("Raiz do Segundo Número: ", resultado)

#------------

nota1: float
nota2: float
nota3: float
media: float

nota1 = float(input("Digite a Nota1: "))
nota2 = float(input("Digite a Nota2: "))
nota3 = float(input("Digite a Nota3: "))

media = (nota1 + nota2 + nota3) / 3

print("A Média é:", media)