#### 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
##### a. Para homens: $P = 72,7h - 58$
##### b. Para mulheres: $P = 62,1h - 44,7$
print("\nCalculo do peso ideal")
# variável
altura = float(input("Digite a altura: "))
# calcular o peso ideal
homem = 72.7 * altura - 58
mulher = 62.1 * altura - 44.7
# exibe o peso ideal
print(f"Uma pessoa com a altura de: {altura}m")
print(f"Se Homem, peso ideal: {homem:.2f}kg")
print(f"Se mulher, peso ideal: {mulher:.2f}kg")