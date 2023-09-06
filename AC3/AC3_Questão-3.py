# Caso A seja informado como 0 -> A = 0 
a = int(input("Informe o valor de A: "))
if a == 0:
    print("Informe um valor diferente")
else:
    b = int(input("Informe o valor de B: "))
    c = int(input("Informe o valor de C: "))

delta = (b ** 2) - (4 * a * c)

# Caso o Delta seja um número negativo
if delta < 0:
    print("A equação não possuiu raizes reais")
else:
    x1 = ((-b + delta ** 0.5) / (2 * a))
    x2 = ((-b - delta ** 0.5) / (2 * a))

# Se x1 ou x2 forem 0
if delta == 0:
    print("Essa equação só tem uma raiz real =", x1)

# Se o Delta for positivo
else:
    print("Essa equação possuiu 2 raizes reais -> x1 =", x1, "x2 =", x2)
