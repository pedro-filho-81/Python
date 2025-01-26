#### 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
##### Calcule o salário bruto (horas * salario por hora)
##### Calcule o desconto do IR (11% do salário bruto)
##### Calcule o desconto do INSS (8% do salário bruto)
##### Calcule o desconto do sindicato (5% do salário bruto)
##### Calcule o salário líquido (salário bruto - descontos)

print("\nCalcula o salário mensal")

# entrada de dados
valor_das_hora = float(input("Informe o valor da hora R$ "))
horas_trabalhadas = float(input("Quantas horas trabalhou? "))

#####  Calcule o salário bruto (horas * salario por hora)
salario_bruto = valor_das_hora * horas_trabalhadas
##### Calcule o desconto do IR (11% do salário bruto)
desc_IR = salario_bruto * 0.11
##### Calcule o desconto do INSS (8% do salário bruto)
inss = salario_bruto * 0.08
##### Calcule o desconto do sindicato (5% do salário bruto)
sindicato = salario_bruto * 0.05
##### Calcule o salário líquido (salário bruto - descontos)
salario_liquido = salario_bruto - (sindicato + inss + desc_IR)

# exibi o resultado
print("\n******************************")
print(f"Valor da hora R$ {valor_das_hora}\nhoras trabalhadas {horas_trabalhadas}\nSalário bruto R$ {salario_bruto:.2f}")
print(f"\nDescontos:\nIR R$ {desc_IR:.2f}\nINSS R$ {inss:.2f}\nSindicato R$ {sindicato:.2f}")
print(f"\nSalário líquido R$ {salario_liquido:.2f}")
print("******************************")