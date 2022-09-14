#adivinhação de palavras
# claudio imai
# 14/09/2022
# ver1.0
import random

nome= input ("Qual o seu nome? ")
print("Boa sorte ! ", nome, "tente adivinhar oque tem na sopa")
palavras= ["batata","cenoura","chuchu","tomate", "repolho","cebola"]
palavra = random.choice(palavras)

print("Adivinhe as letras")
letras = ''
chances = 12

while chances > 0:
    failed = 0
    for char in palavra:
        if char in letras:
            print(char)
        else:
            print("_")
            failed += 1
    if failed ==0:
        print("Você ganhou!!!")
        print ("A palavra é: ", palavra)
        break

    letra = input("digite uma letra:")
    letras += letra

    if letra not in palavra:
        chances -=1
        print("Errado")
        print("Você tem", +chances, 'mais tentativas')

        if chances == 0:
            print("Você perdeu!!!")