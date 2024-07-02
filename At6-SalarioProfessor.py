import os
os.system("cls")

print("Olá, professor da escola Aprender! Vamos calcular seu sálario essa semana!")
nivel=int(input("Digite qual é o seu nível de professor:"))
aulas=int(input("Digite quantas aulas você deu essa semana:"))

if nivel == 1:
    salario=12*aulas
    print("O seu salário essa semana é R$",salario)
elif nivel == 2:
    salario=17*aulas
    print("O seu salário essa semana é R$",salario)
elif nivel == 3:
    salario=25*aulas
    print("O seu salário essa semana é R$",salario)
else:
    print("Erro! Confira o seu nível de professror!")
