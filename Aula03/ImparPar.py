x: int
resto: int

x = int(input("Digite um número: "))

resto = x % 2   # % para dividir e trazer o resto também!


if resto == 0 :
  print("O número é par")
else :                            # else significa "se não"
  print("O número é Ímpar")