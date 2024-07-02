import os
os.system("cls")

print("Com base no valor digitado, vamos descobrir se ele é positivo ou negativo")
numero=float(input("Digite o valor:"))

if numero> 0:
    print("O número",numero,"é positivo!")
elif numero< 0:
    print("O número",numero,"é negativo!")
else:
    print("O número",numero,"é igual a zero!")