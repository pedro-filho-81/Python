#### 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: $P = 72,7h - 58$
print("\nCalculo do peso ideal")
# variável
altura = float(input("Digite a altura: "))
# calcular o peso ideal
peso_ideal = 72.7 * altura - 58
# exibe o peso ideal
print(f"Uma pessoa com {altura}m \nseu peso ideal é de: {peso_ideal:.2f}kg\n") 
