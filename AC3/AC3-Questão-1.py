salario = float(input('Salário do colaborador: '))

if (salario <= 280):
        percentual = 20
elif (salario <= 700):
        percentual = 15
elif (salario <= 1500):
        percentual = 10
else: percentual = 5

print('Salario antigo: R$ ', salario)
print('Percentual para receber: ',percentual,'%')

percentual = percentual/100.0
aumento = percentual * salario
novo_salario = salario + aumento
    
print('Aumento recebido: R$ ',aumento)
print('Novo salário total: R$ ', novo_salario)
