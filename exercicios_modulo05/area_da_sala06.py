#### 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.
print("\n\nÁrea da sala")
# entrada de dados
largura = float(input("Informe a largura da sala:"))
comprim = float(input("Digite o comprimento da sala: "))
# calcular
area = largura * comprim * 3.14159
# exibir
print(f"A área de sala é de {area}m²")