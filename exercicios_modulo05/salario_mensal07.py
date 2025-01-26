#### 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print("\nSalário mensal.")
# entrada de dados
salario = float(input("Informe o valor do salário: "))
horas_trabalho = int(input("Digite as horas trabalhadas: "))
# calcular
novo_salario = salario * horas_trabalho
# exibir
print(f"Novo salário R$ {novo_salario}")