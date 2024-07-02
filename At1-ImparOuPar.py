import os
os.system("cls")
print("Descubra se o npumero é par ou ímpar!")

numero=float(input("Digite um número:"))

resultado = numero % 2

if resultado == 0:
    print(numero,"é um número par!")
else:
    print(numero,"é um número ímpar!")