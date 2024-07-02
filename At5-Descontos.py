import os
os.system("cls")

nome=input("Digite o nome do produto:")
valor=float(input("Digite o valor unitário do produto:"))
quant=int(input("Digite a quantidade desejada:"))

totalint=valor*quant

if quant <= 5:
    total=totalint-(totalint/100)*2
    print("O valor seria igual R$",totalint," Mas você recebeu um desconto de 2% \n Sua compra ficou R$",total)

elif quant>5 or quant<=10:
    total=totalint-(totalint/100)*3
    print("O valor seria igual R$",totalint," Mas você recebeu um desconto de 3% \n Sua compra ficou R$",total)
          
elif quant>10:
    total=totalint-(totalint/100)*5
    print("O valor seria igual R$",totalint," Mas você recebeu um desconto de 5% \n Sua compra ficou R$",total)
else:
    print("Erro! Tente digitar novamente!")