import os
os.system("cls")

print("Com base em dois números vamos descobrir qual é maior e qual é menor!")
v1= float(input("Digite o primeiro valor:"))
v2=float(input("Digite o segundo valor:"))

if v1>v2:
    print(v1,"é o número maior e",v2,"é o número menor")
elif v2>v1:
    print(v2,"é o número maior e",v1,"é o número menor")
else:
    print(v1,"é igual a",v2)