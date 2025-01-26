#### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.
print("\nCalcula a média de 4 notas")
#entrada de dados
nt1 = float(input("Digite Nota1: "))
nt2 = float(input("Nota2: "))
nt3 = float(input("Nota3: "))
nt4 = float(input("Nota4: "))
# calcular
soma = nt1 + nt2 + nt3 + nt4
media = soma / 4
# resultado
print(f"A média das notas = {media}")