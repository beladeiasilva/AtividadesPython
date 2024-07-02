import os
os.system("cls")

print("Vamos fazer um calculo de dois números!")
v1=float(input("Digite o primeiro número:"))
operacao=input("Digite a operação que deseja realiza: \n Multiplicar (x) \n Somar(+) \n Dividir(/) \n Subtrair(-)\n")
v2=float(input("Digite o segundo número:"))

if operacao == "+" or operacao == "somar" :
    resul=v1+v2
    print(v1,"+",v2,"=",resul)

elif operacao == "-" or operacao=="subtrair":
    resul=v1-v2
    print(v1,"-",v2,"=",resul)

elif operacao=="x" or operacao=="mutiplicar" or operacao=="*":
    resul=v1*v2
    print(v1,"x",v2,"=",resul)

elif operacao=="/" or operacao== "dividir":
    resul=v1/v2
    print(v1,"/",v2,"=",resul)

else:
    print("Erro! Tente digitar novamente")
