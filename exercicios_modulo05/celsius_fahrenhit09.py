#### 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. $F = \frac{9}{5}C + 32$

print("\nConverte graus Celsius em graus Fahrenhit.")
# variável recebe valor do usuário
celsius = float(input("Digite a temperatural em graus celsius: "))
# converte o valor de Celsius para Fahrenhit
fahrenhit = celsius * 1.8 + 32
# exibe resultado com uma casas decimais
print(f"{celsius:.1f}°C equivale a {fahrenhit:.1f}°F\n") 