"""

Exercicios Curso Python Udemy parte 3 por Douglas Magalhães

"""

# 1 Faça um programa que mostre os 5 primeiros multiplos de 3.

x = 3
cont = 1
while cont <= 5:
     print(x)
     x = x + 3
     cont += 1

# 2 Escreva um programa que escreva na tela de 1 até 100, de 1 em 1, 3 vezes. A primeira vez deve
# usar for e a segunda while e a terceira do while.

i = 0
n = 0
i2 = 1
for n in range(100):
     print(n - 1)
         while i < 100:
             print(i)
             i = i + 1
             while True:
                 print(i2)
                 i2 = i2 + 1
                 if(i2 > 100):
                     break

# 3 Faça um algoritimo utilizando o comando while que mostra uma contagem regressiva na tela,
# iniciando em 10 e terminando em 0, depois imprimir FIM no final da contagem.

i = 10
while i > 0:
    print(i)
    i = i - 1
        if i == 0:
            print("FIM")



