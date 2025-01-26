#### 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. $C = \frac{5}{9}(F-32)$

print("\nConverte graus Fahrenhit em graus Celsius.")
# variável recebe valor do usuário
fahrehit = float(input("Digite a temperatural em graus fahrenheit: "))
# converte o valor de fahrenhit para celsius
celsius = (fahrehit - 32) / 1.8
# exibe resultado com duas casas decimais
print(f"{fahrehit}°F equivale a {celsius:.2f}°C\n") 